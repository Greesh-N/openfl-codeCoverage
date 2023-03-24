import sys
from openfl.experimental.interface import FLSpec, Aggregator, Collaborator
from openfl.experimental.runtime import LocalRuntime
from openfl.experimental.placement import aggregator, collaborator
from openfl.experimental.utilities.ui import InspectFlow


class HelloFlow(FLSpec):
    """
    A flow where OpenFL prints 'Hi'.

    Run this flow to validate that Metaflow is installed correctly.

    """

    @aggregator
    def start(self):
        """
        This is the 'start' step. All flows must have a step named 'start' that
        is the first step in the flow.

        """
        self.collaborators = self._runtime.collaborators
        print("HelloFlow is starting.")
        self.next(self.task_A, foreach="collaborators")

    @collaborator
    def task_A(self):
        """
        A step for metaflow to introduce itself.
        """
        print("This is task A function")
        self.next(self.task_B)

    @collaborator
    def task_B(self):
        """
        A step for metaflow to introduce itself.

        """
        print("This is task B function")
        self.next(self.join)

    @aggregator
    def join(self, inputs):
        """
        Join function

        """
        print("Hi! This is the join function")
        self.next(self.end)

    @aggregator
    def end(self):
        """
        This is the 'end' step. All flows must have an 'end' step, which is the
        last step in the flow.

        """
        print("HelloFlow is all done.")


if __name__ == "__main__":
    # Setup participants
    aggregator = Aggregator()
    aggregator.private_attributes = {}

    # Setup collaborators with private attributes
    collaborator_names = ["Portland", "Chandler"]  # , "Bangalore", "Delhi"]
    collaborators = [Collaborator(name=name) for name in collaborator_names]

    local_runtime = LocalRuntime(
        aggregator=aggregator, collaborators=collaborators, backend="ray"
    )

    print(f"Local runtime collaborators = {local_runtime.collaborators}")

    flflow = HelloFlow(checkpoint=True)
    flflow.runtime = local_runtime
    for i in range(3):
        print(f"Starting round {i}...")
        flflow.run()

if flflow._checkpoint:
    InspectFlow(flflow, flflow._run_id, show_html=True)
