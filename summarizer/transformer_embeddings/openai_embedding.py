import os
import openai
import tenacity
import httpx

def get_default_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key is None:
        raise ValueError("OPENAI_API_KEY is not set")
    
    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    proxy = os.getenv("OPENAI_PROXY")
    
    return openai.Client(
        api_key=api_key,
        base_url=base_url,
        http_client=httpx.Client(proxy=proxy)
    )

class OpenAIEmbedding:
    def __init__(self, client: openai.Client = None, model: str = "text-embedding-3-small") -> None:
        if client is None:
            self.client = get_default_openai_client()
        else:
            self.client = client
        self.model = model
    
    @tenacity.retry(stop=tenacity.stop_after_attempt(3), wait=tenacity.wait_exponential(multiplier=1, min=4, max=15))
    def __call__(self, text: list[str]) -> list[list[float]]:
        response = self.client.embeddings.create(input=text, model=self.model)
        embeddings = [
            item.embedding for item in sorted(response.data, key=lambda x: x.index)
        ]
        return embeddings