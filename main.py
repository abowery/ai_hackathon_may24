# To run: ACTIONS_MODULE=my_actions python main.py

import os
from pathlib import Path

from asyncflows import AsyncFlows

async def main():
    examples_dir = Path(os.path.dirname(__file__))
    configuration_flow_path = examples_dir / "configuration.yaml"

    # Load the flow from the file
    flow = AsyncFlows.from_file(configuration_flow_path).set_vars(
      question="summarise results",
    )

    # Run the flow
    result = await flow.run()

    # Print the result
    print(result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
