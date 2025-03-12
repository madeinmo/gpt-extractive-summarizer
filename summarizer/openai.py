from summarizer.transformer_embeddings.openai_embedding import OpenAIEmbedding
from summarizer.text_processors.sentence_handler import SentenceHandler
from summarizer.summary_processor import SummaryProcessor

class OpenAISummarizer(SummaryProcessor):
    def __init__(
        self, 
        model: OpenAIEmbedding = OpenAIEmbedding(), 
        sentence_handler: SentenceHandler = SentenceHandler(), 
        random_state: int = 42
    ):
        super().__init__(
            model,
            sentence_handler,
            random_state
        )
        
    def __call__(
        self, 
        body: str,
        ratio: float = 0.2,
        min_length: int = 40,
        max_length: int = 600,
        algorithm: str = 'kmeans',
        num_sentences: int = None,
        return_as_list: bool = False
    ) -> str:
        return super().__call__(body, ratio, min_length, max_length, False, algorithm, num_sentences, return_as_list)
