# Generative AI, RAG, Agentic AI, ML & System Design — Interview Question Guide

> Purpose: This file explains each important interview question in two ways:
>
> 1. **Understand the Question Deeply** — basic explanation, concepts, why interviewer asks it, and what you should know.
> 2. **Interview Answer** — a clear, concise answer you can say directly in an interview.

---

# 1. What is Generative AI?

## Understand the Question Deeply

Generative AI is a branch of AI that creates new content instead of only predicting labels or making decisions.

Traditional AI usually answers questions like:

- Is this email spam or not?
- Is this transaction fraud or not?
- What will the sales be next month?

Generative AI answers questions like:

- Write an email reply.
- Summarize this document.
- Generate code.
- Create an image.
- Generate chatbot responses.

Generative AI models learn patterns from huge datasets and then generate new text, images, audio, video, or code that looks similar to the learned data.

The interviewer asks this to check whether you understand the basic difference between predictive AI and content-generating AI.

## Interview Answer

Generative AI is a type of artificial intelligence that can generate new content such as text, images, code, summaries, audio, or video based on the patterns it learned from training data. Unlike traditional AI, which mostly predicts or classifies, Generative AI creates new outputs. For example, a traditional model may classify a review as positive or negative, while a Generative AI model can write a full response to that review.

---

# 2. How is Generative AI different from Traditional AI?

## Understand the Question Deeply

Traditional AI mainly focuses on:

- Classification
- Prediction
- Regression
- Recommendation
- Clustering
- Fraud detection
- Sentiment analysis

Generative AI focuses on:

- Text generation
- Summarization
- Question answering
- Code generation
- Image generation
- Chatbots
- Document automation

Example:

For customer reviews:

- Traditional AI: “This review is positive.”
- Generative AI: “This customer liked the product quality but complained about delivery. Suggested response: ...”

Traditional AI usually gives structured outputs such as labels, numbers, or scores. Generative AI gives human-like content.

## Interview Answer

Traditional AI is mainly used for prediction, classification, and decision-making, while Generative AI is used to create new content. For example, a traditional ML model can classify customer feedback as positive or negative, but a Generative AI model can summarize the feedback, generate a reply, and suggest next actions. Traditional AI is usually task-specific, whereas Generative AI models like LLMs are more flexible and can handle many language-based tasks.

---

# 3. What is a Large Language Model?

## Understand the Question Deeply

A Large Language Model, or LLM, is a model trained on huge amounts of text data to understand and generate human-like language.

Examples:

- GPT
- Claude
- Gemini
- LLaMA
- Mistral

LLMs are usually based on Transformer architecture. They predict the next token based on previous tokens.

Important concepts:

- **Token**: A small unit of text. It can be a word, part of a word, or symbol.
- **Context window**: The maximum amount of text the model can consider at once.
- **Parameters**: Internal learned values of the model.
- **Transformer**: Architecture that helps the model understand relationships between words using attention.

LLMs are called “large” because they have many parameters and are trained on massive datasets.

## Interview Answer

A Large Language Model is an AI model trained on large amounts of text data to understand and generate language. It is usually based on Transformer architecture and works by predicting the next token based on the given context. LLMs are useful for tasks like question answering, summarization, code generation, translation, and chatbots. Examples include GPT, Claude, Gemini, LLaMA, and Mistral.

---

# 4. What is the difference between LLM and SLM?

## Understand the Question Deeply

LLM means Large Language Model. SLM means Small Language Model.

LLM:

- Bigger model
- More parameters
- Better reasoning
- More general-purpose
- Higher cost
- Higher latency
- Needs more compute

SLM:

- Smaller model
- Faster
- Cheaper
- Easier to deploy locally
- Good for narrow tasks
- Lower reasoning ability compared to LLM

Example:

If you need a chatbot for complex legal reasoning, use LLM. If you need simple intent classification or FAQ matching, SLM may be enough.

## Interview Answer

An LLM is a large model with more parameters and stronger general reasoning capability, while an SLM is a smaller model optimized for speed, cost, and specific tasks. LLMs are better for complex reasoning, summarization, and open-ended generation. SLMs are useful when latency, cost, privacy, or local deployment matters, especially for domain-specific or narrow workflows.

---

# 5. What are common use cases of Generative AI?

## Understand the Question Deeply

Common business use cases include:

- Customer support chatbot
- Document summarization
- Legal assistant
- HR assistant
- Code generation
- Test case generation
- Marketing content generation
- Sales email generation
- Knowledge base question answering
- Invoice extraction and explanation
- Fraud investigation support
- Incident triage
- Report generation

The interviewer wants to know whether you can connect GenAI with real business problems.

## Interview Answer

Common Generative AI use cases include customer support automation, document summarization, knowledge base search using RAG, code generation, marketing content creation, HR chatbots, legal document assistance, invoice processing, and incident triage. In enterprise systems, GenAI is especially useful when users need natural-language interaction with complex internal data.

---

# 6. How would you explain Generative AI to a non-technical stakeholder?

## Understand the Question Deeply

For non-technical people, avoid terms like tokens, embeddings, transformers, vector databases.

Use a simple analogy.

Example:

“Generative AI is like a smart assistant that has read a lot of information and can help draft, summarize, answer, or create content.”

The interviewer checks whether you can communicate technical ideas clearly.

## Interview Answer

I would explain Generative AI as a smart assistant that can create useful content from instructions. For example, it can read a long document and summarize it, draft an email, answer customer questions, or generate reports. It does not just search for existing text; it generates a new response based on the user’s request and available context.

---

# 7. What is Prompt Engineering?

## Understand the Question Deeply

Prompt engineering means writing better instructions for an AI model to get better output.

A good prompt may include:

- Role: “Act as a senior backend engineer.”
- Task: “Explain this API flow.”
- Context: “This is a Node.js Express service.”
- Format: “Give answer in bullet points.”
- Constraints: “Do not assume missing data.”
- Examples: Few-shot examples

Bad prompt:

“Explain RAG.”

Better prompt:

“Explain RAG for an invoice search system. Include ingestion, chunking, embeddings, retrieval, generation, and failure cases.”

## Interview Answer

Prompt engineering is the process of designing clear and structured instructions for an AI model so that it gives accurate and useful responses. A good prompt includes context, the expected role, task, constraints, output format, and examples when needed. It improves quality without changing the model itself.

---

# 8. What is Fine-tuning?

## Understand the Question Deeply

Fine-tuning means taking a pre-trained model and training it further on domain-specific examples.

Example:

A general LLM knows English and coding. If we fine-tune it on customer support tickets, it can learn the company’s tone, categories, and response style.

Fine-tuning is useful when:

- You need consistent output format
- You need domain-specific writing style
- You need specialized behavior
- You have enough high-quality training data

Fine-tuning is not always needed. For many company knowledge tasks, RAG is better because the information changes often.

## Interview Answer

Fine-tuning means further training a pre-trained model on domain-specific data so that it performs better for a specific task or style. It is useful when we need consistent behavior, domain-specific tone, or specialized output format. However, if the requirement is to answer from frequently changing company documents, I would usually prefer RAG instead of fine-tuning.

---

# 9. Fine-tuning vs RAG: When is Fine-tuning better than RAG?

## Understand the Question Deeply

RAG gives the model external knowledge at runtime.

Fine-tuning changes the model’s behavior through training.

Use RAG when:

- Knowledge changes frequently
- You need citations
- You need document-grounded answers
- You do not want to retrain the model

Use fine-tuning when:

- You need a specific style
- You need structured output
- You need domain behavior
- You need repeated task-specific performance
- You have high-quality labeled data

Example:

Company policy Q&A → RAG  
Company-specific tone for email replies → Fine-tuning  
Medical report classification format → Fine-tuning  
Legal document search → RAG

## Interview Answer

Fine-tuning is better when we want to change the model’s behavior, tone, format, or task-specific performance. RAG is better when we want the model to answer from external or frequently changing knowledge. For example, if I need the model to follow a company-specific response style, fine-tuning can help. But if I need it to answer from updated invoices, policies, or internal documents, RAG is better because it retrieves fresh context without retraining.

---

# 10. What is RAG?

## Understand the Question Deeply

RAG means Retrieval-Augmented Generation.

It combines:

1. Retrieval from external documents
2. Generation by an LLM

Basic RAG flow:

1. Upload documents
2. Extract text
3. Split text into chunks
4. Convert chunks into embeddings
5. Store embeddings in vector database
6. User asks a question
7. Convert question into embedding
8. Find similar chunks
9. Send chunks + question to LLM
10. Generate grounded answer

RAG solves:

- Hallucination
- Missing private company knowledge
- Need for citations
- Need to use updated documents

## Interview Answer

RAG, or Retrieval-Augmented Generation, is an approach where we retrieve relevant information from external data sources and pass that context to an LLM to generate an answer. The typical flow is document ingestion, chunking, embedding creation, vector storage, similarity search, and then answer generation using the retrieved chunks. It is useful because it reduces hallucination and allows the model to answer from private or updated company data without retraining.

---

# 11. How would you design RAG for an invoice system?

## Understand the Question Deeply

This is a system design question.

The interviewer wants you to explain the complete pipeline.

Important components:

- File upload
- OCR or PDF text extraction
- Data cleaning
- Chunking
- Metadata tagging
- Embedding generation
- Vector DB
- Query processing
- Retrieval
- Reranking
- LLM answer generation
- Citations
- Access control
- Evaluation
- Monitoring

Invoice-specific metadata:

- Invoice number
- Vendor
- Date
- Amount
- GST/tax
- Customer ID
- PO number
- Payment status

Challenges:

- OCR errors
- Table extraction
- Duplicate invoices
- Multi-page invoices
- Different invoice formats
- Access control
- Hallucination
- Wrong chunk retrieval

## Interview Answer

For an invoice RAG system, I would first build an ingestion pipeline where invoices are uploaded, text is extracted using PDF parsing or OCR, and important metadata like invoice number, vendor, date, amount, and customer ID is captured. Then I would split the text into meaningful chunks, generate embeddings, and store them in a vector database along with metadata.

At query time, I would convert the user question into an embedding, retrieve relevant invoice chunks using similarity search and metadata filters, optionally rerank the results, and pass the top chunks to the LLM with a strict prompt to answer only from the retrieved context. I would also include citations, confidence score, access control, logging, and evaluation to reduce hallucination and improve reliability.

---

# 12. What are OCR challenges in RAG?

## Understand the Question Deeply

OCR means Optical Character Recognition. It extracts text from images or scanned PDFs.

OCR problems:

- Misread characters
- Broken table structure
- Wrong column mapping
- Missing text
- Poor image quality
- Handwritten text errors
- Multi-language issues
- Rotated pages
- Header/footer noise

Example:

Invoice amount `₹10,000` may become `?10,OOO`.

If OCR is wrong, RAG will retrieve wrong data and the LLM may produce wrong answers.

## Interview Answer

OCR can introduce several issues such as incorrect character recognition, broken table structure, missing fields, wrong column mapping, and noise from headers or footers. In invoice systems, this is risky because values like invoice number, date, tax, and amount must be accurate. To handle this, I would use OCR confidence scores, validation rules, table extraction tools, manual review for low-confidence documents, and structured metadata extraction before sending data into the RAG pipeline.

---

# 13. Do 100 one-page documents need Big Data processing?

## Understand the Question Deeply

This checks whether you over-engineer.

100 one-page documents do not need Spark, Hadoop, distributed processing, or heavy big-data systems.

Simple pipeline is enough:

- Store documents
- Extract text
- Chunk
- Embed
- Store in vector DB
- Search

Big data tools are needed when:

- Millions of documents
- Huge volume
- High throughput
- Distributed ingestion
- Complex analytics

## Interview Answer

No, 100 one-page documents do not require big-data processing. A simple pipeline using normal backend services, object storage, text extraction, embeddings, and a vector database would be enough. I would only consider distributed big-data processing if the document volume, ingestion rate, or processing complexity becomes very high.

---

# 14. Why do we need KNN or vector search instead of simple question similarity?

## Understand the Question Deeply

Simple keyword matching works when user query and document use the same words.

Example:

User: “payment due date”  
Document: “invoice settlement deadline”

Keyword matching may fail because words are different but meaning is similar.

Embeddings convert text into vectors that capture semantic meaning.

KNN means K-Nearest Neighbors. It finds the closest vectors to the query vector.

Why useful:

- Semantic search
- Handles synonyms
- Better for natural language
- Finds meaning, not just keywords

## Interview Answer

Simple keyword similarity works only when the user question and document use similar words. But in real systems, users may ask the same thing using different words. KNN with embeddings helps because it searches based on semantic meaning. We convert the question and document chunks into vectors and retrieve the nearest chunks based on distance or similarity. This gives better results for natural-language queries.

---

# 15. Walk me through the KNN process in RAG.

## Understand the Question Deeply

KNN means finding the top K closest vectors.

Steps:

1. Convert document chunks into embeddings
2. Store embeddings in vector DB
3. Convert user query into embedding
4. Compare query vector with stored vectors
5. Calculate similarity
6. Return top K closest chunks
7. Send those chunks to LLM

Example:

User asks: “What is the payment due date for invoice 123?”

The system retrieves chunks from invoice 123 that mention due date, payment terms, and invoice summary.

## Interview Answer

In a RAG pipeline, first we convert all document chunks into embeddings and store them in a vector database. When a user asks a question, we convert the question into an embedding as well. Then KNN search compares the query vector with stored chunk vectors and returns the top K most similar chunks. These chunks are passed to the LLM as context so that it can generate a grounded answer.

---

# 16. What distance metric would you use for vector similarity?

## Understand the Question Deeply

Common similarity metrics:

## Cosine Similarity

Measures angle between two vectors. Good for text embeddings.

Formula:

```text
cosine_similarity(A, B) = (A · B) / (||A|| × ||B||)
```

## Euclidean Distance

Measures straight-line distance between vectors.

## Dot Product

Measures vector alignment and magnitude. Often used in modern embedding search.

For text embeddings, cosine similarity is commonly used because it focuses on direction/meaning more than magnitude.

## Interview Answer

For text embeddings, I would commonly use cosine similarity because it measures the angle between vectors and works well for semantic similarity. It helps identify whether two pieces of text have similar meaning even if their length or magnitude differs. Depending on the embedding model and vector database, dot product or Euclidean distance can also be used, but cosine similarity is a strong default for text-based RAG systems.

---

# 17. How do you calculate cosine similarity between two vectors?

## Understand the Question Deeply

Formula:

```text
cosine_similarity = dot_product(A, B) / (magnitude(A) * magnitude(B))
```

Example:

A = [1, 2]  
B = [3, 4]

Dot product:

```text
1*3 + 2*4 = 11
```

Magnitude A:

```text
sqrt(1² + 2²) = sqrt(5)
```

Magnitude B:

```text
sqrt(3² + 4²) = 5
```

Cosine similarity:

```text
11 / (sqrt(5) * 5)
```

## Interview Answer

Cosine similarity is calculated by taking the dot product of two vectors and dividing it by the product of their magnitudes. The formula is: cosine similarity equals A dot B divided by magnitude of A multiplied by magnitude of B. In text embeddings, higher cosine similarity means the two texts are semantically closer.

---

# 18. What is a Vector Database?

## Understand the Question Deeply

A vector database stores embeddings.

Traditional DB:

- Stores rows, columns, strings, numbers
- Searches exact values or indexes

Vector DB:

- Stores high-dimensional vectors
- Searches by similarity
- Supports nearest-neighbor search

Examples:

- Pinecone
- Weaviate
- Milvus
- Qdrant
- Chroma
- FAISS
- pgvector

Used in:

- RAG
- Semantic search
- Recommendation
- Image similarity
- Chatbot memory

## Interview Answer

A vector database is a database designed to store and search high-dimensional vectors such as embeddings. In a RAG system, document chunks are converted into embeddings and stored in a vector database. When a user asks a question, the query is also embedded, and the vector database retrieves the most similar chunks using similarity search. Examples include Pinecone, Weaviate, Milvus, Qdrant, Chroma, FAISS, and pgvector.

---

# 19. How would you choose a Vector Database?

## Understand the Question Deeply

Criteria:

- Scale
- Latency
- Cost
- Cloud vs self-hosted
- Metadata filtering
- Hybrid search
- Security
- Multi-tenancy
- Ease of integration
- Observability
- Backup and recovery

Examples:

- For quick local prototype: Chroma or FAISS
- For Postgres-based app: pgvector
- For production managed service: Pinecone
- For open-source scalable deployment: Qdrant, Weaviate, Milvus

## Interview Answer

I would choose a vector database based on scale, latency, cost, deployment model, metadata filtering, security, and integration needs. For a simple prototype, FAISS or Chroma may be enough. If the application already uses Postgres, pgvector is a good option. For large-scale production, I would consider Pinecone, Qdrant, Weaviate, or Milvus depending on whether we prefer managed or self-hosted infrastructure.

---

# 20. What is Embedding?

## Understand the Question Deeply

An embedding is a numerical representation of text, image, audio, or other data.

Example:

Text: “payment due date”  
Embedding: `[0.12, -0.45, 0.88, ...]`

Embeddings capture meaning.

Similar meanings have nearby vectors.

Example:

“car” and “vehicle” will be close in vector space.  
“car” and “banana” will be far.

Embeddings are used for:

- Search
- Recommendations
- RAG
- Clustering
- Similarity comparison

## Interview Answer

An embedding is a numerical vector representation of data such as text, image, or audio. It captures semantic meaning, so similar concepts are placed closer in vector space. In RAG, we convert document chunks and user questions into embeddings, then use similarity search to retrieve the most relevant chunks.

---

# 21. Embedding vs Encoding

## Understand the Question Deeply

Encoding is a broad term. It means converting data from one format to another.

Examples of encoding:

- One-hot encoding
- Label encoding
- Token encoding
- Base64 encoding
- UTF-8 encoding

Embedding is a specific kind of representation where data is converted into dense vectors that capture meaning.

One-hot encoding:

```text
cat = [1, 0, 0]
dog = [0, 1, 0]
car = [0, 0, 1]
```

Embedding:

```text
cat = [0.21, -0.52, 0.73, ...]
dog = [0.25, -0.48, 0.70, ...]
```

Embeddings capture similarity. One-hot does not.

## Interview Answer

Encoding is a broad process of converting data into another representation. One-hot encoding, label encoding, and token encoding are all examples of encoding. Embedding is a more advanced representation where data is converted into dense vectors that capture semantic meaning. So embedding can be considered a type of encoding, but not all encodings are embeddings.

---

# 22. Is One-Hot Encoding the same as Encoding?

## Understand the Question Deeply

No.

One-hot encoding is one type of encoding.

Encoding is the general category.

One-hot encoding represents categories as binary vectors.

Problem with one-hot:

- Sparse
- High-dimensional
- Does not capture meaning
- No similarity between related words

Example:

One-hot cannot understand that “king” and “queen” are related. Embeddings can.

## Interview Answer

One-hot encoding is not the same as encoding. Encoding is a general term for converting data into a machine-readable format. One-hot encoding is one specific encoding technique where each category is represented as a binary vector. It is simple but sparse and does not capture semantic similarity.

---

# 23. How do embeddings come into LSTM?

## Understand the Question Deeply

LSTM is a sequence model used before Transformers became dominant.

LSTM works with numerical input, not raw text.

So text must be converted into vectors first.

Flow:

1. Tokenize text
2. Convert tokens into embeddings
3. Feed embedding sequence into LSTM
4. LSTM processes sequence
5. Output classification or prediction

Example sentiment analysis:

```text
"I love this product"
↓
tokens
↓
embeddings
↓
LSTM
↓
positive sentiment
```

Embedding layer can be:

- Pre-trained: Word2Vec, GloVe, FastText
- Trainable: learned during model training

## Interview Answer

LSTM cannot directly process raw text, so tokens are converted into numerical vectors first. This is where embeddings come in. Each word or token is represented as an embedding vector, and the sequence of embeddings is passed to the LSTM. The LSTM then learns sequential patterns from those vectors. So embeddings act as the input representation for the LSTM.

---

# 24. How would you classify 500 reviews? ML or GenAI?

## Understand the Question Deeply

This checks decision-making.

For only 500 reviews, options:

## Traditional ML

Good if:

- Labels are available
- Need cheap, fast classification
- Output is simple: positive/negative/neutral
- Need predictable behavior

Models:

- Logistic Regression
- Naive Bayes
- SVM
- Random Forest
- Fine-tuned small model

## GenAI

Good if:

- Need explanation
- Need summarization
- Need theme extraction
- Need flexible categories
- No labeled data
- Need quick prototype

## Hybrid

Use GenAI to label or summarize, then train ML model later.

## Interview Answer

If the task is only to classify 500 reviews as positive, negative, or neutral, I would first check whether labeled data exists and how accurate the output needs to be. For simple classification, traditional ML or even a pre-trained sentiment model may be enough because it is cheaper, faster, and more predictable. If we also need explanations, summaries, topic extraction, or dynamic categories, I would use Generative AI. A practical approach is to use GenAI for quick analysis or labeling, and then use a smaller ML model for scalable repeated classification.

---

# 25. What is Sentiment Analysis?

## Understand the Question Deeply

Sentiment analysis means identifying emotion or opinion in text.

Common labels:

- Positive
- Negative
- Neutral

Advanced labels:

- Happy
- Angry
- Frustrated
- Confused
- Complaint
- Appreciation

Use cases:

- Product reviews
- Customer support tickets
- Social media monitoring
- Survey feedback
- App reviews

Approaches:

- Rule-based
- Traditional ML
- Deep learning
- Transformer models
- GenAI

## Interview Answer

Sentiment analysis is an NLP task where we identify the emotional tone or opinion in text, such as positive, negative, or neutral. It is commonly used for customer reviews, support tickets, social media, and survey feedback. Depending on the complexity, it can be implemented using rule-based methods, traditional ML models, Transformer-based models, or Generative AI.

---

# 26. What are Transformers and why are they called Transformers?

## Understand the Question Deeply

Transformers were introduced in the paper “Attention Is All You Need” in 2017.

Before Transformers, NLP used RNNs and LSTMs. These processed text sequentially, which was slow and struggled with long-range dependencies.

Transformers changed this by using attention to process tokens in parallel and learn relationships between all tokens.

They are called Transformers because they transform input sequences into contextual representations.

Example:

In the sentence:

```text
The animal did not cross the road because it was tired.
```

The model learns that “it” refers to “animal.”

Key concepts:

- Self-attention
- Multi-head attention
- Positional encoding
- Encoder-decoder architecture
- Parallel processing

## Interview Answer

Transformers are neural network architectures introduced in 2017 in the paper “Attention Is All You Need.” They use self-attention to understand relationships between tokens in a sequence. They are called Transformers because they transform input tokens into contextual representations. Compared to RNNs and LSTMs, Transformers can process tokens in parallel and handle long-range dependencies better, which made them very effective for NLP and later for LLMs.

---

# 27. What is Attention Mechanism?

## Understand the Question Deeply

Attention helps a model decide which words are important for understanding another word.

Example:

```text
The cat sat on the mat because it was tired.
```

To understand “it,” the model should pay attention to “cat.”

Self-attention compares each token with every other token.

Problem:

If there are `n` tokens, attention compares all pairs.

Complexity:

```text
O(n²)
```

For long documents, this becomes expensive.

## Interview Answer

Attention is a mechanism that allows a model to focus on the most relevant tokens while processing a sequence. In self-attention, each token attends to other tokens to build contextual meaning. This helps the model understand dependencies between words, even when they are far apart in the sentence. However, standard attention has O(n²) complexity because every token is compared with every other token.

---

# 28. How would you solve attention complexity?

## Understand the Question Deeply

Standard attention is expensive for long context because complexity is O(n²).

Ways to reduce complexity:

- Sparse attention
- Sliding window attention
- Local attention
- Linear attention
- Chunking long documents
- Retrieval-based approach
- Long-context optimized models
- Summarization before processing
- Hierarchical processing

In production, for enterprise documents, RAG is often better than putting everything into context.

## Interview Answer

Standard attention has O(n²) complexity, so for long inputs I would avoid sending everything directly to the model. Practical solutions include chunking documents, using RAG to retrieve only relevant context, using sliding-window or sparse attention models, summarizing long documents, or using long-context optimized models. In enterprise applications, RAG is often the most practical approach because it reduces context size and cost.

---

# 29. What is Context Window?

## Understand the Question Deeply

Context window is how much text the model can consider at once.

If model has 8k token context, it can only process around that many tokens in one request.

Problems with small context:

- Cannot fit long documents
- May lose earlier conversation
- Cannot reason over all data at once

Solutions:

- Chunking
- RAG
- Summarization
- Memory
- Long-context models

## Interview Answer

A context window is the maximum number of tokens an LLM can process in a single request, including input and output. If the document or conversation is larger than the context window, we need techniques like chunking, summarization, RAG, or memory management to provide only the most relevant information to the model.

---

# 30. What are Hallucinations in GenAI?

## Understand the Question Deeply

Hallucination means the model gives an answer that sounds correct but is false or unsupported.

Example:

User asks about a company policy. Model invents a policy that does not exist.

Causes:

- Missing context
- Weak prompt
- Model guessing
- Poor retrieval
- Ambiguous question
- Outdated training data

Solutions:

- RAG
- Citations
- Answer only from provided context
- Confidence scoring
- Human review
- Evaluation datasets
- Guardrails

## Interview Answer

Hallucination happens when a GenAI model generates information that sounds confident but is incorrect or not supported by the source data. To reduce hallucination, I would use RAG with reliable retrieved context, strict prompting, citations, confidence scoring, answer validation, and human review for high-risk workflows.

---

# 31. Text Hallucination vs Functional Hallucination

## Understand the Question Deeply

Text hallucination:

- Model writes false information.
- Example: “The invoice was paid on March 10” when it was not.

Functional hallucination:

- Model calls the wrong tool or performs the wrong action.
- Example: Instead of checking order status, it triggers refund.

Functional hallucination is more dangerous in agentic systems because the model can take actions.

## Interview Answer

Text hallucination is when the model generates incorrect or unsupported text. Functional hallucination is when an AI agent performs or suggests an incorrect action, such as calling the wrong API or using a tool incorrectly. Functional hallucination is more risky because it can affect real systems, so it needs strict tool permissions, validation, human approval, and audit logs.

---

# 32. How do you evaluate a Generative AI model's performance?

## Understand the Question Deeply

GenAI evaluation is harder than normal ML because answers may vary.

Evaluation methods:

- Human evaluation
- Groundedness
- Relevance
- Faithfulness
- Accuracy
- Toxicity check
- Bias check
- Latency
- Cost
- User feedback
- Task completion rate
- Citation correctness

For RAG:

- Retrieval precision
- Retrieval recall
- Answer groundedness
- Citation accuracy
- Hallucination rate

## Interview Answer

I would evaluate a Generative AI model using both automated and human evaluation. Important metrics include answer relevance, factual accuracy, groundedness, hallucination rate, citation correctness, latency, cost, and user satisfaction. For RAG systems, I would separately evaluate retrieval quality and generation quality. In domain-specific systems, human review by domain experts is very important.

---

# 33. What are Evals in Agentic AI?

## Understand the Question Deeply

Evals are tests for AI systems.

They check if the AI:

- Gives correct answers
- Uses tools correctly
- Does not hallucinate
- Follows safety rules
- Completes tasks
- Does not enter loops
- Handles edge cases

Agentic AI evals are more complex because agents take actions.

Test cases may include:

- Input
- Expected tool call
- Expected final answer
- Safety expectations
- Allowed actions
- Failure handling

## Interview Answer

Evals are structured tests used to measure whether an AI or agentic system is behaving correctly. In agentic systems, evals should check not only final answers but also tool usage, reasoning flow, safety, permissions, loop prevention, and failure handling. They help ensure that the system is reliable before deploying it to production.

---

# 34. Precision vs Recall

## Understand the Question Deeply

Precision and recall are classification metrics.

## Precision

Out of predicted positives, how many were actually positive?

Example cheating detection:

If system flags 100 students as cheaters and 80 are actually cheaters:

```text
Precision = 80 / 100 = 80%
```

High precision means fewer innocent users are wrongly flagged.

## Recall

Out of actual positives, how many did we catch?

If there are 200 actual cheaters and system catches 80:

```text
Recall = 80 / 200 = 40%
```

High recall means fewer cheaters escape.

Trade-off:

- For cheating detection, false accusation is serious, so precision is very important.
- But recall also matters to catch most cheaters.

## Interview Answer

Precision tells us how many predicted positives are actually correct, while recall tells us how many actual positives we successfully captured. In cheating detection, high precision is important because wrongly accusing innocent users is harmful. At the same time, recall is also important to catch real cheaters. The right balance depends on business risk and whether flagged cases go through human review.

---

# 35. Bias vs Variance

## Understand the Question Deeply

Bias and variance explain model errors.

High bias:

- Model is too simple
- Underfits data
- Performs badly on training and test data

High variance:

- Model is too complex
- Overfits training data
- Performs well on training data but badly on test data

Goal:

- Low bias
- Low variance
- Good generalization

## Interview Answer

Bias is error caused by overly simple assumptions in the model, leading to underfitting. Variance is error caused by the model being too sensitive to training data, leading to overfitting. A good model balances bias and variance so that it performs well on both training and unseen test data.

---

# 36. Overfitting vs Underfitting

## Understand the Question Deeply

Underfitting:

- Model is too simple
- Cannot learn patterns
- Bad train accuracy
- Bad test accuracy

Overfitting:

- Model memorizes training data
- Good train accuracy
- Bad test accuracy

Solutions for overfitting:

- More data
- Regularization
- Dropout
- Early stopping
- Cross-validation
- Simpler model

Solutions for underfitting:

- Better features
- More complex model
- Train longer
- Reduce regularization

## Interview Answer

Underfitting happens when the model is too simple and fails to learn patterns, so it performs poorly on both training and test data. Overfitting happens when the model memorizes training data and performs well on training data but poorly on unseen data. We handle overfitting with regularization, more data, early stopping, and cross-validation.

---

# 37. Correlation

## Understand the Question Deeply

Correlation measures relationship between two variables.

Example:

- More study hours may correlate with higher marks.
- Higher temperature may correlate with higher AC usage.

Correlation range:

```text
-1 to +1
```

- +1: strong positive relation
- -1: strong negative relation
- 0: no linear relation

Important:

Correlation does not mean causation.

Example:

Ice cream sales and drowning cases may both increase in summer, but ice cream does not cause drowning.

## Interview Answer

Correlation measures the strength and direction of relationship between two variables. A positive correlation means both increase together, while a negative correlation means one increases as the other decreases. However, correlation does not prove causation, so we should be careful before making business decisions based only on correlation.

---

# 38. Random Forest

## Understand the Question Deeply

Random Forest is an ensemble ML algorithm.

It builds many decision trees and combines their outputs.

For classification:

- Majority vote

For regression:

- Average prediction

Why good:

- Reduces overfitting compared to single decision tree
- Handles non-linear data
- Works well with tabular data
- Gives feature importance

Key idea:

Many weak/medium trees together give stronger performance.

## Interview Answer

Random Forest is an ensemble algorithm that builds multiple decision trees and combines their predictions. For classification, it uses majority voting, and for regression, it averages the outputs. It reduces overfitting compared to a single decision tree and works well for tabular datasets. It also helps understand feature importance.

---

# 39. R² and Adjusted R²

## Understand the Question Deeply

R² measures how much variance in target variable is explained by the model.

Example:

R² = 0.80 means model explains 80% of the variance.

Problem:

R² can increase when you add more features, even if they are useless.

Adjusted R² solves this by penalizing unnecessary features.

Use:

- R² for basic model fit
- Adjusted R² when comparing models with different number of features

## Interview Answer

R² measures how much of the variance in the target variable is explained by the model. Adjusted R² improves on this by penalizing unnecessary features, so it is more reliable when comparing models with different numbers of input variables. If R² increases but Adjusted R² decreases, it may mean the new feature is not useful.

---

# 40. Lemmatization

## Understand the Question Deeply

Lemmatization converts words to their base dictionary form.

Examples:

```text
running → run
better → good
studies → study
```

It is used in NLP preprocessing.

Difference from stemming:

- Stemming cuts words crudely
- Lemmatization uses vocabulary and grammar

Example:

Stemming may convert `studies` to `studi`  
Lemmatization converts `studies` to `study`

## Interview Answer

Lemmatization is an NLP preprocessing technique that converts words to their base or dictionary form. For example, “running” becomes “run” and “studies” becomes “study.” It is more linguistically accurate than stemming because it considers vocabulary and grammar.

---

# 41. WebSockets vs REST API

## Understand the Question Deeply

REST:

- Request-response model
- Client asks, server replies
- Good for normal CRUD APIs
- Example: get user profile, update product

WebSocket:

- Persistent connection
- Server can push data anytime
- Good for real-time apps
- Example: chat, live dashboard, stock price, IoT status

In your project, you can mention:

- REST for CRUD and configuration
- WebSockets/MQTT for real-time status updates

## Interview Answer

REST is a request-response communication model where the client sends a request and the server returns a response. It is good for CRUD operations. WebSocket keeps a persistent connection open between client and server, allowing real-time two-way communication. It is useful for chat, live dashboards, notifications, IoT status updates, or any feature where the server needs to push updates instantly.

---

# 42. How would you build a dashboard application? HLD

## Understand the Question Deeply

A dashboard usually has:

Frontend:

- React/Next.js
- Charts
- Tables
- Filters
- Search
- Pagination
- Real-time updates

Backend:

- REST APIs
- WebSocket APIs
- Auth
- Aggregation services
- Database queries
- Cache

Database:

- Transaction DB
- Analytics DB
- Time-series DB if needed

Other components:

- Queue
- Scheduler
- Monitoring
- Access control

## Interview Answer

For a dashboard application, I would design a React or Next.js frontend with reusable components for charts, tables, filters, and real-time status sections. The backend would expose REST APIs for normal data fetching and WebSockets for real-time updates. Data would be stored in a database, and for heavy analytics I would use pre-aggregated tables or caching. I would also include authentication, role-based access control, pagination, monitoring, and error handling.

---

# 43. How would you calculate whether a GenAI response is good or not?

## Understand the Question Deeply

Response quality can be measured by:

- Relevance
- Correctness
- Completeness
- Groundedness
- Citation accuracy
- User satisfaction
- Toxicity
- Format following
- Latency
- Cost

For RAG:

- Did it retrieve correct chunks?
- Did answer use only retrieved chunks?
- Did it cite correct sources?
- Did it hallucinate?

## Interview Answer

I would evaluate response quality using relevance, factual accuracy, completeness, groundedness, citation correctness, format compliance, latency, and user feedback. For RAG systems, I would separately measure retrieval quality and answer quality. I would also maintain a test dataset of expected questions and use human review for domain-critical answers.

---

# 44. Coding Task: Find a string or substring in 1 million strings

## Understand the Question Deeply

Problem:

You have an array/list of 1 million strings. You need to search whether a string or substring exists.

Simple solution:

Loop through all strings and check substring.

Time complexity:

```text
O(n * m)
```

Where:

- n = number of strings
- m = average string length

For one-time search, loop is okay.

For repeated searches, optimize with:

- Inverted index
- Trie
- Suffix tree
- Full-text search engine
- Elasticsearch/OpenSearch
- Database full-text index

Interviewers ask this to check whether you know the difference between one-time search and repeated production search.

## Interview Answer

If it is a one-time search over 1 million strings, I would iterate through the list and check whether the substring exists in each string. The time complexity would be O(n × m), where n is the number of strings and m is average string length. If this search is frequent in production, I would build an index, use a trie for prefix search, or use a full-text search engine like Elasticsearch or OpenSearch for scalable substring and keyword search.

---

# 45. YOLO Model

## Understand the Question Deeply

YOLO means “You Only Look Once.”

It is an object detection model.

It detects:

- What object is present
- Where it is located

Output includes:

- Bounding box coordinates
- Class label
- Confidence score

Example:

Image has a dog and a car.

YOLO outputs:

```json
[
  {"class": "dog", "confidence": 0.94, "box": [x, y, width, height]},
  {"class": "car", "confidence": 0.88, "box": [x, y, width, height]}
]
```

YOLO is fast because it detects objects in one forward pass.

## Interview Answer

YOLO stands for You Only Look Once. It is a real-time object detection model that identifies objects and their locations in an image in a single forward pass. It outputs bounding boxes, class labels, and confidence scores. It is commonly used in real-time detection use cases like surveillance, autonomous systems, traffic analysis, and video analytics.

---

# 46. How does YOLO give bounding box details?

## Understand the Question Deeply

YOLO divides an image into grids and predicts bounding boxes.

Output usually contains:

- x center
- y center
- width
- height
- objectness score
- class probabilities

After prediction:

- Low confidence boxes are removed
- Non-Maximum Suppression removes duplicate boxes
- Final boxes are returned

## Interview Answer

YOLO predicts bounding boxes directly from the image. The model output includes coordinates such as x-center, y-center, width, and height, along with object confidence and class probabilities. After prediction, low-confidence boxes are filtered out and Non-Maximum Suppression is applied to remove duplicate overlapping boxes. The final result contains object class, confidence score, and bounding box coordinates.

---

# 47. What is Agentic AI?

## Understand the Question Deeply

Agentic AI means AI systems that can plan, use tools, take actions, and work toward goals.

Normal chatbot:

- Answers questions

Agentic AI:

- Understands goal
- Plans steps
- Calls tools/APIs
- Observes result
- Updates plan
- Completes task

Example:

Goal: “Resolve this customer ticket.”

Agent can:

1. Read ticket
2. Classify issue
3. Search knowledge base
4. Check customer account
5. Draft reply
6. Escalate if needed

## Interview Answer

Agentic AI refers to AI systems that can work toward a goal by planning, using tools, taking actions, observing results, and adjusting their behavior. Unlike a simple chatbot that only responds with text, an agent can interact with APIs, databases, search systems, and other tools to complete multi-step tasks.

---

# 48. Agentic AI vs Traditional AI

## Understand the Question Deeply

Traditional AI:

- Usually performs one task
- Reactive
- Predicts or classifies
- No long-term goal

Agentic AI:

- Goal-oriented
- Multi-step reasoning
- Tool usage
- Memory
- Planning
- Execution

Example:

Traditional AI: Classify ticket as billing issue.  
Agentic AI: Classify ticket, retrieve billing policy, check invoice, draft reply, create refund request if approved.

## Interview Answer

Traditional AI usually performs a specific prediction or classification task. Agentic AI is more goal-oriented and can plan multiple steps, use tools, maintain state, and take actions to complete a task. For example, a traditional model may classify a support ticket, while an agentic system can classify it, retrieve documents, check account data, draft a response, and escalate if needed.

---

# 49. Andrew Ng’s 4 Agentic Design Patterns

## Understand the Question Deeply

The commonly discussed agentic patterns are:

1. **Reflection**  
   Agent reviews and improves its own output.

2. **Tool Use**  
   Agent calls external APIs, search, database, calculator, etc.

3. **Planning**  
   Agent breaks a complex task into smaller steps.

4. **Multi-agent Collaboration**  
   Multiple agents work together, each with a specialized role.

## Interview Answer

The four common agentic design patterns are reflection, tool use, planning, and multi-agent collaboration. Reflection means the agent reviews and improves its own work. Tool use means it can call APIs or external systems. Planning means it breaks a task into steps. Multi-agent collaboration means multiple specialized agents coordinate to solve a larger problem.

---

# 50. What is ReAct Framework?

## Understand the Question Deeply

ReAct means Reason + Act.

The model alternates between:

- Reasoning about what to do
- Taking an action using a tool
- Observing the result
- Continuing until done

Example:

Question: “What is the status of invoice 123?”

Agent:

1. Thinks: Need invoice data
2. Action: Call invoice API
3. Observation: Invoice unpaid
4. Answer: Invoice 123 is unpaid

## Interview Answer

ReAct stands for Reason and Act. It is an agent pattern where the model reasons about the next step, takes an action using a tool, observes the result, and continues until it reaches the final answer. It is useful for tasks that require external information or multi-step tool usage.

---

# 51. System Prompt vs User Prompt

## Understand the Question Deeply

System prompt:

- High-priority instruction
- Defines role, rules, safety, behavior
- Hidden or controlled by application

User prompt:

- User’s request
- Lower priority than system prompt

Example:

System prompt: “You are a banking assistant. Never reveal account data without authentication.”  
User prompt: “Show me another user’s balance.”

System prompt must override unsafe user prompt.

## Interview Answer

A system prompt defines the assistant’s role, rules, safety boundaries, and behavior. It has higher priority and is controlled by the application. A user prompt is the actual request from the user. In production systems, system prompts are important for guardrails, security, tone, and compliance, while user prompts provide the task-specific instruction.

---

# 52. How is Reflection implemented in Agentic AI?

## Understand the Question Deeply

Reflection means model checks its own output.

Implementation:

1. Generate answer
2. Send answer to evaluator prompt/model
3. Check for errors, missing parts, hallucination
4. Revise answer
5. Return final output

Can use:

- Same model
- Separate critic model
- Rule-based validator
- Human review

## Interview Answer

Reflection can be implemented by adding a review step after the initial output. The agent generates a response, then a critic or evaluator checks it for correctness, completeness, hallucination, formatting, and policy compliance. If issues are found, the system asks the model to revise the answer before returning it. For critical workflows, reflection can be combined with rule-based validation or human review.

---

# 53. Tool Use and Function Calling

## Understand the Question Deeply

Function calling allows the AI to call external tools.

Examples:

- Search database
- Create ticket
- Send email
- Fetch invoice
- Run calculation
- Trigger deployment

Important:

- Tool schema
- Input validation
- Permissions
- Error handling
- Audit logs
- Human approval for risky actions

## Interview Answer

Tool use or function calling allows an AI model to interact with external systems through predefined APIs or functions. The model decides which tool to call and provides structured arguments. In production, I would define strict schemas, validate inputs, limit permissions, log all tool calls, handle errors, and require human approval for risky actions.

---

# 54. Short-term vs Long-term Memory in Agentic AI

## Understand the Question Deeply

Short-term memory:

- Current conversation
- Current task state
- Temporary context

Long-term memory:

- User preferences
- Past decisions
- Historical tickets
- Learned facts
- Stored in database/vector DB

Example:

Customer support agent:

- Short-term: current ticket ID
- Long-term: customer’s previous issues and preferences

## Interview Answer

Short-term memory is the temporary context used during the current task or conversation, such as current ticket ID, user request, or intermediate steps. Long-term memory stores persistent information such as user preferences, past interactions, or historical decisions. In production, long-term memory should be controlled carefully with privacy, access control, and data retention policies.

---

# 55. Multi-Agent Orchestration and Routing

## Understand the Question Deeply

Multi-agent system means multiple specialized agents work together.

Example:

- Planner agent
- Retriever agent
- Coding agent
- Validation agent
- Execution agent

Routing decides which agent should handle which task.

Challenges:

- Latency
- Cost
- Coordination
- State sharing
- Failure handling
- Infinite loops
- Debugging

## Interview Answer

Multi-agent orchestration is the process of coordinating multiple specialized agents to solve a task. Routing decides which agent should handle each step based on task type, context, or confidence. It improves modularity for complex workflows, but it also adds latency, cost, orchestration complexity, and failure-handling challenges.

---

# 56. LangChain vs LangGraph vs AutoGen vs CrewAI

## Understand the Question Deeply

## LangChain

Good for building LLM pipelines, chains, tools, retrievers, memory.

## LangGraph

Good for stateful, graph-based agent workflows with controlled execution.

## AutoGen

Good for multi-agent conversations and research-style agent collaboration.

## CrewAI

Good for role-based agents with tasks and workflows.

Simple view:

- LangChain: LLM app framework
- LangGraph: stateful agent workflow graph
- AutoGen: multi-agent conversations
- CrewAI: role/task-based agent teams

## Interview Answer

LangChain is useful for building LLM applications with chains, tools, retrievers, and memory. LangGraph is better when we need stateful, graph-based agent workflows with controlled execution and cycles. AutoGen focuses on multi-agent conversation patterns, while CrewAI focuses on role-based agent teams and task delegation. For production workflows that need control and state management, I would prefer LangGraph.

---

# 57. What is LangChain?

## Understand the Question Deeply

LangChain is a framework for building LLM apps.

It provides:

- Prompt templates
- Chains
- Agents
- Tools
- Memory
- Retrievers
- Document loaders
- Vector DB integrations

Example:

You can build a PDF chatbot using LangChain with:

- PDF loader
- Text splitter
- Embedding model
- Vector store
- Retriever
- LLM
- Prompt template

## Interview Answer

LangChain is a framework for building LLM-powered applications. It provides components like prompt templates, chains, agents, tools, memory, document loaders, retrievers, and vector database integrations. It is commonly used for building RAG systems, chatbots, and tool-using AI applications.

---

# 58. What is LangGraph?

## Understand the Question Deeply

LangGraph is used to build stateful agent workflows as graphs.

In LangGraph:

- Nodes are steps or agents
- Edges define flow
- State is passed between nodes
- Conditional routing is possible
- Cycles are supported

Good for:

- Agent workflows
- Multi-step systems
- Human approval flows
- Retry loops
- Controlled tool execution

## Interview Answer

LangGraph is a framework for building stateful, graph-based LLM and agent workflows. Each node represents a step or agent, and edges define how the workflow moves. It is useful when we need controlled execution, conditional routing, memory/state management, retries, and human-in-the-loop workflows.

---

# 59. Multi-Agent vs Single-Agent Architecture

## Understand the Question Deeply

Single-agent:

- Simpler
- Lower latency
- Easier debugging
- Lower cost
- Good for simple workflows

Multi-agent:

- Better separation of responsibilities
- Specialized agents
- Better for complex workflows
- More modular
- But higher latency and complexity

Customer support example:

Single-agent can handle simple FAQ.

Multi-agent may be better when:

- Ticket classification
- Document retrieval
- Policy validation
- Account lookup
- Response generation
- Compliance review

## Interview Answer

I would choose a single-agent system if the workflow is simple, latency-sensitive, and does not require many specialized steps. I would choose a multi-agent system if the task is complex and benefits from role separation, such as classification, retrieval, validation, and response generation. Multi-agent systems improve modularity but add orchestration complexity, cost, latency, and more failure points.

---

# 60. Planner vs Executor Roles

## Understand the Question Deeply

Planner:

- Decides what to do
- Maintains state
- Breaks task into steps
- Controls workflow

Executor:

- Performs specific action
- Calls tools
- Often stateless
- Replaceable

Why separate?

- Better control
- Safer execution
- Easier debugging
- Failure isolation

Without separation:

- Tool calls may become uncontrolled
- State may be lost
- Agent may take wrong actions
- Harder to audit

## Interview Answer

The planner should decide the overall strategy, maintain task state, and control the workflow, while the executor should perform specific actions like calling APIs or tools. This separation improves safety, control, debugging, and failure isolation. If we do not separate them, the system may mix planning with execution, leading to uncontrolled tool calls, poor state management, and harder debugging.

---

# 61. How would you automate customer support using GenAI?

## Understand the Question Deeply

Complete flow:

1. User raises ticket
2. Classify ticket
3. Detect intent
4. Retrieve relevant docs
5. Check customer data if needed
6. Generate response
7. Validate answer
8. Human review if confidence low
9. Send response
10. Log feedback

Important:

- RAG for company knowledge
- Human escalation
- Guardrails
- PII protection
- Tone control
- Monitoring

## Interview Answer

I would build a GenAI customer support system using ticket classification, RAG-based knowledge retrieval, customer context lookup, response generation, validation, and human escalation. Simple and high-confidence tickets can be auto-answered, while complex or risky cases should go to human agents. I would include guardrails, PII protection, audit logs, feedback collection, and continuous evaluation.

---

# 62. How would you ensure marketing content aligns with brand voice?

## Understand the Question Deeply

Brand voice means consistent tone and style.

Examples:

- Friendly
- Professional
- Youthful
- Premium
- Technical
- Simple

How to ensure:

- Brand guidelines in prompt
- Few-shot examples
- Approved content library
- Review workflow
- Fine-tuning if needed
- Evaluation checklist

## Interview Answer

I would provide the model with clear brand guidelines, tone instructions, approved examples, and restricted vocabulary if needed. I would use prompt templates and few-shot examples to guide the output. For production, I would add human approval, automated checks, and evaluation against brand criteria. If the style must be very consistent at scale, fine-tuning can also be considered.

---

# 63. How would you handle biased or offensive AI output?

## Understand the Question Deeply

Bias/offensive output is a safety issue.

Solutions:

- Content moderation
- Toxicity detection
- Bias testing
- Guardrails
- Safe prompts
- Human review
- User reporting
- Dataset review
- Logging and monitoring

## Interview Answer

I would handle biased or offensive output using multiple layers: safe system prompts, content moderation filters, toxicity and bias detection, output validation, and human review for sensitive cases. I would also log such incidents, analyze the root cause, improve prompts or data, and continuously evaluate the model against safety test cases.

---

# 64. How would you implement document summarization using GenAI?

## Understand the Question Deeply

For small documents:

- Send document to model
- Ask for summary

For long documents:

- Split into chunks
- Summarize each chunk
- Combine summaries
- Generate final summary

Types:

- Short summary
- Executive summary
- Bullet summary
- Action items
- Risk summary

Challenges:

- Long context
- Missing details
- Hallucination
- Wrong emphasis

## Interview Answer

For document summarization, I would first check document size. For small documents, I can send the full content to the model with a structured prompt. For long documents, I would use chunking and hierarchical summarization: summarize each chunk, then combine those summaries into a final summary. I would also ask the model to preserve key facts, avoid unsupported claims, and produce the output in the required format.

---

# 65. How would you use GenAI to improve software development productivity?

## Understand the Question Deeply

Use cases:

- Code generation
- Test case generation
- Code review
- Documentation
- API documentation
- Bug explanation
- Query generation
- Log analysis
- Refactoring suggestions
- Onboarding assistant

Risks:

- Wrong code
- Security bugs
- License issues
- Over-reliance

## Interview Answer

GenAI can improve software development productivity through code generation, test case generation, documentation, code review assistance, bug analysis, refactoring suggestions, and onboarding support. I would use it as an assistant, not as an automatic replacement for engineering review. Generated code should still go through testing, code review, security checks, and CI/CD validation.

---

# 66. How would you build a legal assistant using GenAI?

## Understand the Question Deeply

Legal assistant must be very careful.

Architecture:

- RAG over legal docs
- Citations required
- Access control
- No unsupported legal advice
- Human lawyer review
- Audit logs
- Versioned documents
- Jurisdiction filters

## Interview Answer

For a legal assistant, I would use a RAG-based architecture where legal documents are ingested, chunked, embedded, and retrieved based on the user query. The model should answer only from retrieved legal sources and provide citations. I would include jurisdiction filters, access control, audit logs, confidence scoring, and human legal review for critical outputs. The assistant should avoid unsupported legal advice.

---

# 67. What are Diffusion Models?

## Understand the Question Deeply

Diffusion models are used for image generation.

They work by:

1. Starting with noise
2. Gradually removing noise
3. Producing image

Examples:

- Stable Diffusion
- DALL·E-style image generation models
- Midjourney-like systems

Concept:

Training learns how to reverse noise into meaningful images.

## Interview Answer

Diffusion models are generative models commonly used for image generation. They learn to generate data by starting from random noise and gradually denoising it into a meaningful image. They are widely used in text-to-image generation systems because they can produce high-quality and diverse images.

---

# 68. How would you deploy a GenAI chatbot for HR?

## Understand the Question Deeply

HR chatbot can answer:

- Leave policy
- Benefits
- Payroll questions
- Onboarding
- Company policies

Important:

- RAG over HR docs
- Access control
- PII protection
- Escalation to HR
- Audit logs
- Feedback
- Role-based answers

## Interview Answer

For an HR chatbot, I would use RAG over approved HR policies and company documents. The chatbot should answer only from trusted sources, provide citations when needed, protect employee PII, and apply role-based access control. For sensitive questions, it should escalate to HR. I would also include audit logs, monitoring, feedback collection, and regular document updates.

---

# 69. RLHF — Reinforcement Learning with Human Feedback

## Understand the Question Deeply

RLHF improves model behavior using human feedback.

Flow:

1. Model generates multiple answers
2. Humans rank answers
3. Train reward model
4. Optimize model to produce preferred answers

Used to make models:

- More helpful
- Safer
- More aligned
- Better at following instructions

## Interview Answer

RLHF stands for Reinforcement Learning with Human Feedback. It is a technique where human reviewers rank model outputs, and that feedback is used to train a reward model. The AI model is then optimized to produce responses that humans prefer. RLHF is used to make models more helpful, safe, and aligned with user expectations.

---

# 70. How would you generate synthetic data?

## Understand the Question Deeply

Synthetic data means artificially generated data.

Uses:

- Add training examples
- Balance classes
- Protect privacy
- Simulate rare cases

Risks:

- Unrealistic data
- Bias amplification
- Data leakage
- Poor quality

Steps:

1. Define target distribution
2. Generate data
3. Validate quality
4. Remove sensitive information
5. Test model performance

## Interview Answer

To generate synthetic data, I would first define the target use case, schema, and distribution. Then I would generate data using rules, simulation, or generative models. After generation, I would validate quality, check privacy risks, remove duplicates or sensitive data, and test whether the synthetic data actually improves model performance.

---

# 71. How do you ensure GenAI systems are ethical and unbiased?

## Understand the Question Deeply

Ethical AI includes:

- Fairness
- Privacy
- Transparency
- Accountability
- Safety
- Human oversight

Practical steps:

- Bias testing
- Diverse evaluation set
- Moderation
- Explainability
- Audit logs
- Human review
- Access control
- Data governance

## Interview Answer

I would ensure ethical and unbiased GenAI by using high-quality and representative data, testing outputs for bias, applying content safety filters, protecting user privacy, maintaining audit logs, and adding human review for sensitive workflows. I would also monitor the system continuously and collect feedback to detect harmful patterns after deployment.

---

# 72. How would you design multilingual support using GenAI?

## Understand the Question Deeply

Options:

1. Translate input to English, answer, translate back
2. Use multilingual LLM directly
3. Use language-specific RAG
4. Hybrid approach

Challenges:

- Translation errors
- Cultural nuance
- Different scripts
- Mixed-language queries
- Local compliance

## Interview Answer

For multilingual support, I would first detect the user’s language. Then I would either use a multilingual LLM directly or translate the query into a common language, retrieve relevant knowledge, generate the answer, and translate it back. For high-quality support, I would maintain multilingual knowledge sources, evaluate language-specific accuracy, and handle cultural and regional differences carefully.

---

# 73. Challenges scaling Generative AI in enterprises

## Understand the Question Deeply

Challenges:

- Cost
- Latency
- Rate limits
- Data privacy
- Security
- Hallucination
- Evaluation
- Monitoring
- Multi-tenancy
- Access control
- Model drift
- Prompt injection
- Compliance

## Interview Answer

Scaling GenAI in enterprises involves challenges such as high cost, latency, rate limits, data privacy, access control, hallucination, monitoring, evaluation, and compliance. To handle this, I would use caching, RAG, model routing, batching, observability, guardrails, human review, tenant isolation, and cost monitoring.

---

# 74. How would you use GenAI in fraud detection?

## Understand the Question Deeply

GenAI is not always the main fraud detection model.

Traditional ML is often better for scoring fraud.

GenAI can help with:

- Explaining fraud alerts
- Summarizing evidence
- Analyst assistant
- Pattern discovery
- Report generation
- Natural language investigation

Architecture:

- ML model detects suspicious transaction
- GenAI explains why
- RAG retrieves policies/history
- Analyst reviews

## Interview Answer

For fraud detection, I would usually use traditional ML models for core fraud scoring because they are more measurable and predictable. GenAI can support the workflow by explaining alerts, summarizing evidence, retrieving related cases, generating investigation reports, and helping analysts understand suspicious patterns. For high-risk decisions, I would keep a human review step.

---

# 75. What future trends do you see in GenAI?

## Understand the Question Deeply

Good trends:

- Agentic AI
- Multimodal AI
- Smaller specialized models
- On-device AI
- Better RAG
- AI copilots
- AI workflow automation
- Better evaluation and governance
- Domain-specific AI systems

## Interview Answer

I see GenAI moving toward agentic systems, multimodal models, smaller domain-specific models, better RAG pipelines, on-device AI, and stronger governance. Enterprises will focus more on reliable AI workflows with evaluation, observability, security, and human oversight instead of just simple chatbots.

---

# 76. How would you measure success of a GenAI project in enterprise?

## Understand the Question Deeply

Metrics depend on business goal.

Examples:

Customer support:

- Reduced resolution time
- Deflection rate
- CSAT
- Escalation rate

Document assistant:

- Answer accuracy
- Search time reduction
- Citation correctness

Engineering assistant:

- Developer productivity
- Test coverage
- PR review time

General:

- Cost per request
- Latency
- User adoption
- Error rate
- Hallucination rate

## Interview Answer

I would measure success using both business and technical metrics. Business metrics could include time saved, cost reduction, user adoption, customer satisfaction, and task completion rate. Technical metrics include accuracy, groundedness, hallucination rate, latency, cost per request, error rate, and retrieval quality. The exact metrics should be tied to the business objective.

---

# 77. What is Top-K sampling?

## Understand the Question Deeply

Top-K sampling controls how LLM chooses next token.

The model predicts probability for many possible next tokens.

Top-K means:

- Keep only the top K most likely tokens
- Sample from those
- Ignore the rest

Example:

If K = 5, model only chooses from top 5 likely next tokens.

Low K:

- More focused
- Less creative

High K:

- More diverse
- More creative
- More risk

## Interview Answer

Top-K sampling is a decoding technique where the model restricts the next-token choice to the top K most probable tokens. This reduces randomness by ignoring very unlikely tokens. A smaller K makes output more focused and deterministic, while a larger K allows more diversity and creativity.

---

# 78. What is Top-P / Nucleus Sampling?

## Understand the Question Deeply

Top-P sampling chooses from the smallest set of tokens whose total probability reaches P.

Example:

If P = 0.9, the model selects enough top tokens to cover 90% probability mass, then samples from them.

Top-P is dynamic:

- Sometimes few tokens
- Sometimes many tokens

Top-K is fixed count. Top-P is probability-based.

## Interview Answer

Top-P, also called nucleus sampling, selects the smallest group of tokens whose combined probability reaches a threshold like 0.9. The model then samples from that group. Unlike Top-K, which always uses a fixed number of tokens, Top-P dynamically adjusts the candidate set based on probability distribution.

---

# 79. Temperature in LLMs

## Understand the Question Deeply

Temperature controls randomness.

Low temperature:

- More deterministic
- More focused
- Good for factual answers

High temperature:

- More creative
- More varied
- Higher hallucination risk

Example:

- Temperature 0: deterministic
- Temperature 0.2: factual
- Temperature 0.8: creative
- Temperature 1+: highly random

## Interview Answer

Temperature controls the randomness of model output. Lower temperature makes the model more deterministic and focused, which is useful for factual or enterprise tasks. Higher temperature makes output more creative and diverse but can increase hallucination risk.

---

# 80. How would you design a scalable GenAI system for 100k concurrent users?

## Understand the Question Deeply

This is a big system design question.

Important components:

- Load balancer
- API gateway
- Auth
- Rate limiting
- Queue
- Model gateway
- Caching
- RAG service
- Vector DB
- Database
- Streaming response
- Observability
- Circuit breaker
- Autoscaling
- Cost monitoring

Main challenge:

LLM calls are expensive and slow.

Optimization:

- Cache repeated responses
- Use smaller models for simple tasks
- Async jobs for long tasks
- Streaming
- Rate limits
- Batch requests
- Tenant quotas

## Interview Answer

For 100k concurrent users, I would design the system with an API gateway, load balancer, authentication, rate limiting, request queue, model gateway, RAG service, vector database, caching, and observability. I would use streaming responses for better user experience, cache frequent queries, route simple tasks to smaller models, and use async processing for long-running tasks. I would also add circuit breakers, autoscaling, tenant quotas, monitoring, and cost controls.

---

# 81. How do you implement caching in a GenAI application?

## Understand the Question Deeply

Caching reduces:

- Cost
- Latency
- Repeated LLM calls

Types:

- Exact prompt cache
- Semantic cache
- Retrieval cache
- Embedding cache
- Response cache
- Tool/API result cache

Caution:

- Do not cache sensitive data incorrectly
- Use tenant isolation
- Cache invalidation when documents update

## Interview Answer

I would implement caching at multiple levels: embedding cache for repeated text, retrieval cache for repeated queries, response cache for exact repeated prompts, semantic cache for similar questions, and tool/API result cache for repeated backend calls. I would ensure tenant isolation, TTL, invalidation when documents change, and avoid caching sensitive data insecurely.

---

# 82. Multi-tenant GenAI system considerations

## Understand the Question Deeply

Multi-tenant means many customers use same platform.

Important:

- Data isolation
- Tenant-specific vector indexes
- Metadata filters
- Auth and RBAC
- Quotas
- Rate limits
- Billing
- Monitoring per tenant
- Prompt customization
- Encryption
- Audit logs

Risk:

One tenant should never retrieve another tenant’s data.

## Interview Answer

For a multi-tenant GenAI system, the main considerations are tenant data isolation, access control, vector index separation or strict metadata filtering, per-tenant quotas, rate limits, billing, audit logs, encryption, and monitoring. I would make sure that retrieval queries are always scoped by tenant ID to prevent data leakage across customers.

---

# 83. How do you handle model drift?

## Understand the Question Deeply

Model drift means model performance changes over time.

In GenAI, drift can happen because:

- User behavior changes
- Data changes
- Documents change
- Model provider updates model
- Prompt changes
- Retrieval quality drops

How to handle:

- Continuous evaluation
- Golden test dataset
- User feedback
- Monitoring metrics
- Version prompts/models
- Compare outputs
- Retrain or update system

## Interview Answer

I would handle model drift by continuously monitoring quality metrics such as accuracy, groundedness, hallucination rate, user feedback, retrieval quality, and task success rate. I would maintain a golden evaluation dataset, version prompts and models, compare outputs across versions, and retrain or adjust prompts, retrieval, or model selection when performance drops.

---

# 84. How do you implement a circuit breaker in a GenAI system?

## Understand the Question Deeply

Circuit breaker protects system from repeated failures.

States:

1. Closed: normal operation
2. Open: stop calls because failures are high
3. Half-open: test if service recovered

Use cases:

- LLM provider down
- High latency
- Rate limit errors
- Vector DB failure

Fallbacks:

- Use smaller backup model
- Return cached response
- Show graceful error
- Queue request
- Human escalation

## Interview Answer

A circuit breaker monitors failures and latency for external services like LLM APIs, vector databases, or tool APIs. If failures cross a threshold, the circuit opens and temporarily stops sending requests to that dependency. The system can then use fallback options such as cached responses, backup models, queued processing, or graceful error messages. After some time, it moves to half-open state to test recovery.

---

# 85. Best practices for error handling in GenAI

## Understand the Question Deeply

Errors can happen in:

- LLM API
- Vector DB
- Embedding model
- Tool call
- JSON parsing
- Rate limits
- Timeout
- Bad user input
- Safety filter

Best practices:

- Retry with backoff
- Timeout
- Circuit breaker
- Fallback model
- Validate outputs
- Structured errors
- Log request IDs
- Human escalation
- User-friendly messages

## Interview Answer

For GenAI error handling, I would use timeouts, retries with exponential backoff, circuit breakers, fallback models, structured error responses, output validation, and user-friendly failure messages. I would also log request IDs, model details, prompts metadata, retrieval results, and tool calls for debugging. For critical workflows, I would add human escalation.

---

# 86. Monitoring for GenAI applications

## Understand the Question Deeply

Monitor:

- Latency
- Cost
- Token usage
- Error rate
- Model provider failures
- Retrieval quality
- Hallucination rate
- User feedback
- Tool call success
- Safety violations
- Cache hit rate

Observability:

- Traces
- Spans
- Logs
- Metrics
- Dashboards

## Interview Answer

I would monitor GenAI applications using metrics, logs, and traces. Important metrics include latency, cost, token usage, error rate, cache hit rate, retrieval quality, hallucination rate, user feedback, tool call success rate, and safety violations. I would also use tracing to track the full path from user request to retrieval, model call, tool call, and final response.

---

# 87. Cost optimization in GenAI applications

## Understand the Question Deeply

LLM cost depends on:

- Model choice
- Input tokens
- Output tokens
- Number of requests
- RAG chunks
- Retries
- Tool calls

Optimization:

- Use smaller models for simple tasks
- Cache responses
- Reduce prompt size
- Retrieve fewer chunks
- Summarize context
- Batch requests
- Rate limits
- Token budgets
- Monitor cost per tenant

## Interview Answer

To optimize GenAI cost, I would use model routing, where simple tasks go to smaller cheaper models and complex tasks go to stronger models. I would reduce prompt size, limit retrieved chunks, cache repeated queries, use semantic caching, set token budgets, batch where possible, and monitor cost per user or tenant. Cost optimization should not reduce answer quality for critical workflows.

---

# 88. How would you automate incident triage using GenAI?

## Understand the Question Deeply

Incident triage means identifying what went wrong and what to do.

Flow:

1. Receive alert from Datadog, CloudWatch, Grafana, etc.
2. Classify severity
3. Retrieve logs, metrics, traces
4. Search past incidents
5. Retrieve runbooks
6. Suggest root cause
7. Recommend action
8. Execute safe remediation or ask human approval
9. Create incident report

Important:

- Safe tool execution
- Human approval
- Audit logs
- Rollback
- Confidence score

## Interview Answer

For incident triage, I would ingest alerts from tools like Datadog, CloudWatch, or Grafana, classify severity, retrieve related logs and metrics, search past incidents and runbooks using RAG, and generate a suggested root cause and remediation steps. For safe actions, the system can call APIs automatically, but risky actions should require human approval. I would include audit logs, rollback plans, and monitoring.

---

# 89. Safe Tool Execution in Agentic AI

## Understand the Question Deeply

When agents can call tools, safety is critical.

Risks:

- Delete data
- Send wrong email
- Refund wrong user
- Run dangerous command
- Expose private data

Controls:

- Authentication
- Authorization
- Scoped permissions
- Input validation
- Human approval
- Dry run
- Audit logs
- Rollback
- Rate limits

## Interview Answer

Safe tool execution requires strict authentication, scoped permissions, input validation, audit logs, and approval workflows. The agent should only access tools it needs, following least privilege. Risky actions like deleting data, refunds, deployments, or external communication should require human approval or dry-run mode. Every tool call should be logged for traceability.

---

# 90. Validated RAG Pipelines

## Understand the Question Deeply

Validated RAG means RAG with quality checks.

Validation checks:

- Retrieved chunks are relevant
- Answer is grounded in chunks
- Citations are correct
- Confidence is high
- Access control applied
- No unsupported claims

Useful techniques:

- Reranking
- Metadata filtering
- Citation checks
- Answer verification
- Human review
- Evaluation datasets

## Interview Answer

A validated RAG pipeline ensures that retrieval and generation are both reliable. I would use metadata filtering, reranking, citation generation, confidence scoring, and answer-grounding checks. The model should answer only from retrieved context, and low-confidence or sensitive answers should be escalated to a human.

---

# 91. Human Oversight and Escalation

## Understand the Question Deeply

Human-in-the-loop is needed when:

- Confidence is low
- Action is risky
- Compliance is involved
- Money/legal/health impact exists
- User complains
- Model detects ambiguity

Examples:

- Refund approval
- Legal answer
- Medical advice
- High-severity incident
- Employee termination policy

## Interview Answer

Human oversight should be added for low-confidence, high-risk, or compliance-sensitive cases. The AI system can handle routine tasks, but actions involving money, legal decisions, security, production changes, or sensitive employee data should go through human approval. This improves safety and accountability.

---

# 92. Cheating Detection Strategies in Testing Platform

## Understand the Question Deeply

Ways to detect cheating:

- Tab switching
- Copy-paste detection
- Multiple face detection
- Webcam monitoring
- Screen recording
- Keystroke patterns
- IP/device fingerprinting
- Similar answer detection
- Time pattern anomaly
- Browser focus tracking
- Code similarity
- Voice/noise detection
- External device detection

Need balance:

- Privacy
- False positives
- User consent
- Human review

## Interview Answer

Cheating detection can use multiple signals such as tab switching, copy-paste events, webcam face detection, screen activity, IP/device fingerprinting, answer similarity, keystroke patterns, and abnormal timing behavior. I would not rely on a single signal. I would combine signals into a risk score and send high-risk cases for human review to avoid wrongly accusing innocent users.

---

# 93. How can Graph Databases help detect cheating?

## Understand the Question Deeply

Graph database stores relationships.

Entities:

- Student
- Device
- IP address
- Test session
- Question
- Answer
- Location
- Browser fingerprint

Graph can detect:

- Same IP used by many users
- Same device used by multiple accounts
- Shared answer patterns
- Suspicious clusters
- Common cheating source

Example:

If 20 accounts use same device fingerprint and same answer pattern, graph can reveal the cluster.

## Interview Answer

Graph databases help because cheating often involves relationships between users, devices, IPs, sessions, answers, and locations. A graph model can reveal suspicious clusters, shared devices, common IPs, repeated answer patterns, or coordinated behavior. This is harder to detect with simple row-based analysis because the relationship pattern is the main signal.

---

# 94. How would you design a system to extract code from screen/video and execute it?

## Understand the Question Deeply

This is a complex AI + system design problem.

Flow:

1. User uploads video/screen recording
2. Extract frames
3. Detect code region
4. OCR/code extraction
5. Clean extracted text
6. Detect language
7. Validate code
8. Run in sandbox
9. Capture output/errors
10. Return explanation

Important:

- Sandbox execution
- Timeout
- Resource limits
- No network access
- Security isolation
- Malware prevention

Never run extracted code directly on production server.

## Interview Answer

I would design the system as a pipeline. First, extract frames from the video, detect the code region, use OCR to extract code text, clean and format the code, and detect the programming language. Then I would run the code only inside a secure sandbox or container with strict timeout, CPU/memory limits, no sensitive file access, and restricted network. The system would capture output, errors, and generate an explanation. Security is the most important part because arbitrary code execution is risky.

---

# 95. How would you run code extracted by an LLM safely?

## Understand the Question Deeply

Running arbitrary code is dangerous.

Safe execution needs:

- Docker container
- Firecracker microVM
- gVisor
- No host file access
- No secrets
- Network disabled
- CPU/memory limits
- Timeout
- Logs
- Kill switch

Never trust LLM-generated code.

## Interview Answer

I would never run LLM-extracted code directly on the host. I would execute it in an isolated sandbox such as a container or microVM with no secrets, restricted file system, disabled or limited network access, CPU and memory limits, and strict timeout. I would log execution details and destroy the sandbox after execution.

---

# 96. Enterprise AI System Experience

## Understand the Question Deeply

This question checks practical experience.

You can answer using your AI analytics or RAG-style system experience.

Structure:

1. Business problem
2. Data sources
3. Architecture
4. AI/RAG/LLM usage
5. Evaluation
6. Deployment
7. Monitoring
8. Outcome

## Interview Answer

Yes, I have worked on enterprise-style AI systems where the goal was to convert business or operational data into useful insights. The architecture involved data ingestion, backend APIs, storage, scheduled processing, AI/LLM-based insight generation, and frontend dashboards. For knowledge-based answers, I would use a RAG-style pipeline with embeddings and retrieval. I also focus on monitoring, accuracy, latency, and user feedback because enterprise AI systems need reliability, not just good demos.

---

# 97. What role does data play in GenAI?

## Understand the Question Deeply

Data is important in:

- Model training
- Fine-tuning
- RAG documents
- Evaluation datasets
- User feedback
- Monitoring

Bad data causes:

- Wrong answers
- Bias
- Hallucination
- Poor retrieval
- Poor model behavior

Good data needs:

- Clean format
- Relevant content
- Metadata
- Access control
- Versioning
- Quality validation

## Interview Answer

Data plays a critical role in GenAI. The model’s behavior, retrieval quality, factual accuracy, and evaluation all depend on data quality. For enterprise GenAI, clean documents, good metadata, access control, updated knowledge sources, and evaluation datasets are very important. Poor data can lead to hallucination, bias, and wrong answers.

---

# 98. Traditional ML Models vs GenAI Models

## Understand the Question Deeply

Traditional ML is best for:

- Classification
- Regression
- Fraud scoring
- Forecasting
- Tabular prediction
- Recommendation
- Measurable tasks

GenAI is best for:

- Text generation
- Summarization
- Question answering
- Reasoning over documents
- Natural language interface
- Explanation

Often best solution is hybrid.

Example:

Fraud:

- ML model gives risk score
- GenAI explains why and writes report

## Interview Answer

Traditional ML models are better for structured prediction tasks like classification, regression, forecasting, and fraud scoring. GenAI models are better for language-heavy tasks like summarization, question answering, content generation, and explanation. In many enterprise systems, the best approach is hybrid: ML makes the prediction, and GenAI explains or assists with the workflow.

---

# 99. How would you handle non-deterministic behavior in GenAI?

## Understand the Question Deeply

LLMs may give different answers for same input.

Causes:

- Sampling
- Temperature
- Model updates
- Retrieval differences
- Tool failures

How to control:

- Low temperature
- Fixed prompts
- Version prompts
- Version models
- Structured output schemas
- Evaluation tests
- Guardrails
- Caching
- Human review

## Interview Answer

To handle non-deterministic behavior, I would use low temperature for factual workflows, fixed prompt templates, model and prompt versioning, structured output schemas, automated evals, and caching where appropriate. For critical workflows, I would add validation and human review. The goal is to make outputs predictable enough for production use.

---

# 100. Risks of Infinite Loops and Agent Sprawl

## Understand the Question Deeply

Agent loops happen when agent keeps calling tools or re-planning without finishing.

Agent sprawl means too many agents without clear responsibility.

Problems:

- High cost
- High latency
- Unpredictable behavior
- Hard debugging
- Repeated actions

Solutions:

- Max step limit
- Timeout
- Budget limit
- Clear stop condition
- Tool call limits
- Workflow graph
- Observability

## Interview Answer

Infinite loops happen when an agent keeps reasoning or calling tools without reaching a final state. Agent sprawl happens when too many agents are created without clear responsibilities. I would prevent this using max step limits, timeouts, cost budgets, clear stop conditions, tool call limits, and graph-based orchestration. Observability is also important to debug agent behavior.

---

# 101. Security and Deployment Challenges in Agentic AI

## Understand the Question Deeply

Risks:

- Prompt injection
- Data leakage
- Unauthorized tool calls
- Excessive permissions
- Wrong actions
- Insecure logs
- Compliance issues

Solutions:

- Least privilege
- Tool allowlists
- Input validation
- Output validation
- Human approval
- Tenant isolation
- Audit logs
- Secrets management
- Red-team testing

## Interview Answer

The main security challenges in agentic AI are prompt injection, data leakage, unauthorized tool calls, excessive permissions, and unsafe actions. I would handle this using least-privilege access, tool allowlists, input and output validation, tenant isolation, audit logs, secret management, and human approval for risky operations.

---

# 102. Agentic RAG

## Understand the Question Deeply

Normal RAG:

- Retrieve chunks
- Generate answer

Agentic RAG:

- Agent decides what to retrieve
- May ask follow-up query
- May use multiple tools
- May verify answer
- May rerank or retry retrieval
- May call APIs

Example:

For invoice question, agent may:

1. Search invoice docs
2. Check payment API
3. Compare both
4. Generate final answer

## Interview Answer

Agentic RAG is an advanced RAG approach where an agent controls the retrieval and reasoning process. Instead of doing one fixed retrieval, the agent can decide what to search, refine the query, call tools, verify results, and then generate an answer. It is useful for complex workflows where one retrieval step may not be enough.

---

# 103. How would you integrate GenAI into a customer-facing mobile app?

## Understand the Question Deeply

Mobile app should not directly call LLM provider with secret keys.

Architecture:

- Mobile app
- Backend API
- Auth
- Rate limiting
- LLM gateway
- RAG service
- Safety filter
- Response streaming
- Logging

Consider:

- Latency
- Cost
- Privacy
- Offline behavior
- Abuse prevention
- UX

## Interview Answer

I would integrate GenAI through a secure backend, not directly from the mobile app. The mobile app would call our backend API, which handles authentication, rate limiting, prompt construction, RAG retrieval, LLM calls, safety checks, and logging. I would also optimize for latency using streaming, caching, and smaller models where possible.

---

# 104. How would you shortlist ML vs GenAI for a problem?

## Understand the Question Deeply

Decision factors:

Use ML when:

- Output is label/score/number
- Need explainable metrics
- Data is structured
- Need low cost and high speed

Use GenAI when:

- Output is text/content
- Need summarization
- Need natural language reasoning
- Need flexible interaction

Use hybrid when:

- ML predicts, GenAI explains
- GenAI labels data, ML scales it

## Interview Answer

I would decide based on the output type, data type, cost, latency, accuracy requirements, and explainability. If the task is classification, prediction, or scoring, traditional ML may be better. If the task needs natural language generation, summarization, explanation, or flexible reasoning, GenAI is better. For many enterprise use cases, I would combine both.

---

# 105. Quick Revision Cheat Sheet

## RAG One-Liner

RAG retrieves relevant external knowledge and gives it to the LLM so the answer is grounded and less hallucinated.

## Fine-tuning One-Liner

Fine-tuning changes model behavior using training data; RAG gives the model external knowledge at runtime.

## Embedding One-Liner

Embedding is a dense vector representation that captures semantic meaning.

## Vector DB One-Liner

A vector database stores embeddings and retrieves similar vectors efficiently.

## Cosine Similarity One-Liner

Cosine similarity measures how close two vectors are based on angle.

## Agentic AI One-Liner

Agentic AI plans, uses tools, takes actions, and works toward a goal.

## LangGraph One-Liner

LangGraph builds controlled stateful agent workflows using nodes, edges, and shared state.

## WebSocket One-Liner

WebSocket keeps a persistent connection for real-time two-way communication.

## Precision vs Recall One-Liner

Precision reduces false accusations; recall catches more actual positives.

## YOLO One-Liner

YOLO is a fast object detection model that predicts class, confidence, and bounding boxes in one pass.

---

# 106. Best Interview Strategy

## Understand the Question Deeply

When answering GenAI interview questions, do not only give definitions. Interviewers like practical thinking.

Use this format:

1. Define the concept
2. Explain where it is used
3. Mention trade-offs
4. Give production considerations
5. Give one example

## Interview Answer Template

A strong answer usually sounds like this:

```text
First, I would understand the business requirement and risk level.
If the task needs factual answers from company documents, I would use RAG.
If the task needs consistent style or format, I may consider fine-tuning.
For production, I would add evaluation, monitoring, guardrails, access control,
human review for risky cases, and cost optimization.
```

---

# 107. Your Strong Personal Project Answer for GenAI Interview

## Understand the Question Deeply

You should connect your answer to your experience as a full-stack developer.

You can mention:

- React/Next.js dashboard
- Node/FastAPI backend
- Data ingestion
- Scheduled processing
- AI insights
- RAG/embeddings
- Real-time updates
- Monitoring
- Business value

## Interview Answer

In my project, I worked on an AI-powered analytics and insight platform where the goal was to convert business or engagement data into useful forecasts and natural-language insights. The system had a frontend dashboard built with Next.js/React, backend APIs using FastAPI/Node.js, scheduled ingestion jobs, database storage, and AI-based insight generation. For contextual answers, I would use RAG with embeddings so the system can retrieve relevant historical data before generating insights. I focused on practical production concerns like latency, accuracy, scheduled refresh, monitoring, and making the insights useful for decision-making.

---

# 108. Final Memory Map

## Core GenAI

- GenAI
- LLM
- Prompt engineering
- Fine-tuning
- RAG
- Hallucination
- Context window
- Temperature
- Top-K
- Top-P

## NLP

- Sentiment analysis
- Embedding
- Encoding
- One-hot encoding
- LSTM embeddings
- Lemmatization

## RAG System Design

- OCR
- Chunking
- Embeddings
- Vector DB
- KNN
- Cosine similarity
- Reranking
- Citations
- Access control

## ML Basics

- Bias
- Variance
- Overfitting
- Underfitting
- Correlation
- Random Forest
- R²
- Adjusted R²
- Precision
- Recall

## Agentic AI

- Agentic AI
- ReAct
- Reflection
- Tool use
- Memory
- Multi-agent
- Planner/executor
- LangChain
- LangGraph
- Safe execution

## Production GenAI

- Scaling
- Caching
- Multi-tenancy
- Model drift
- Circuit breaker
- Monitoring
- Error handling
- Cost optimization
- Human oversight

---

# 109. Most Important Answers to Memorize First

1. RAG
2. Fine-tuning vs RAG
3. Embeddings and vector database
4. Cosine similarity
5. LangChain vs LangGraph
6. Agentic AI and ReAct
7. Hallucination and guardrails
8. Scaling GenAI for production
9. Traditional ML vs GenAI
10. Precision vs recall
11. WebSocket vs REST
12. Safe tool execution
13. Multi-agent vs single-agent
14. Attention complexity
15. YOLO output

---

# 110. Short Closing Interview Statement

## Interview Answer

My approach to GenAI systems is practical and production-focused. I first decide whether the problem needs traditional ML, RAG, fine-tuning, or an agentic workflow. Then I design the system with proper data ingestion, retrieval, model usage, evaluation, monitoring, cost control, security, and human oversight. I believe GenAI should not only generate good answers but also be reliable, measurable, safe, and useful for real business workflows.
