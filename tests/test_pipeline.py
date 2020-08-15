import trio

from slurry import Pipeline, Delay, Zip

from .fixtures import produce_increasing_integers, produce_alphabet

async def test_pipeline_create(autojump_clock):
    async with Pipeline.create(None):
        await trio.sleep(1)

async def test_pipeline_passthrough(autojump_clock):
    async with Pipeline.create(produce_increasing_integers(1)) as pipeline:
        result = []
        async with pipeline.tap() as aiter:
            async for i in aiter:
                result.append(i)
        assert result == [0, 1, 2]
