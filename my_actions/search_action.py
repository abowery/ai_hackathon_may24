from asyncflows.actions.base import Action, BaseModel, Field
from duckduckgo_search import DDGS

import aiohttp


class Inputs(BaseModel):
    query: str = Field(
        description="URL of the webpage to GET",
    )


class Outputs(BaseModel):
    result: str = Field(
        description="Text content of the webpage",
    )


class GetURL(Action[Inputs, Outputs]):
    name = "duckduckgo_search"

    async def run(self, inputs: Inputs) -> Outputs:
        results = str(DDGS().text("Top law firms in Oxfordshire UK", max_results=50))
        return Outputs(result=results)
