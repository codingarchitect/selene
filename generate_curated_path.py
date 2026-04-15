import re

# --- CONFIGURATION ---
GITHUB_USER = "codingarchitect"
REPO_NAME = "selene"

# F-String Templates for our base URLs
PAGES_BASE_URL = f"https://{GITHUB_USER}.github.io/{REPO_NAME}"
GITHUB_BASE_URL = f"https://github.com/{GITHUB_USER}/{REPO_NAME}/blob/master"
COLAB_BASE_URL = f"https://githubtocolab.com/{GITHUB_USER}/{REPO_NAME}/blob/master"
# ---------------------

raw_text = """
| (1) Activation Functions[HTML](notebooks/html/nn_activation_functions_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/nn_activation_functions_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/nn_activation_functions_basics_standalone.ipynb) |
| (2) Artificial Neural Networks (Basic Architecture)[HTML](notebooks/html/artificial_neural_networks_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/artificial_neural_networks_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/artificial_neural_networks_basics_standalone.ipynb) |
| (3) Attention & Multi-Head Attention[HTML](notebooks/html/attention_mha_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/attention_mha_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/attention_mha_basics_standalone.ipynb) |
| (4) Backpropagation[HTML](notebooks/html/backpropagation_basic_examples.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/backpropagation_basic_examples.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/backpropagation_basic_examples_standalone.ipynb) |
| (5) Backpropagation (Generalization)[HTML](notebooks/html/backpropagation_generalization.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/backpropagation_generalization.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/backpropagation_generalization_standalone.ipynb) |
| (6) Backpropagation Through Time (BPTT)[HTML](notebooks/html/backpropagation_through_time_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/backpropagation_through_time_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/backpropagation_through_time_basics_standalone.ipynb) |
| (7) Bias & Variance (Machine Learning)[HTML](notebooks/html/bias_variance_ml_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/bias_variance_ml_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/bias_variance_ml_basics_standalone.ipynb) |
| (8) Bias-Variance Decomposition[HTML](notebooks/html/bias_variance_ml_decomposition.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/bias_variance_ml_decomposition.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/bias_variance_ml_decomposition_standalone.ipynb) |
| (9) Building a GPT-Style LLM from Scratch[HTML](notebooks/html/llm_building_gptstyle_llm_from_scratch.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/llm_building_gptstyle_llm_from_scratch.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/llm_building_gptstyle_llm_from_scratch_standalone.ipynb) |
| (10) Building a Word Tokenizer from Scratch[HTML](notebooks/html/word_tokenizer_implementation.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/word_tokenizer_implementation.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/word_tokenizer_implementation_standalone.ipynb) |
| (11) Byte-Pair Encoding Tokenization[HTML](notebooks/html/byte_pair_encoding_tokenization.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/byte_pair_encoding_tokenization.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/byte_pair_encoding_tokenization_standalone.ipynb) |
| (12) Curse of Dimensionality[HTML](notebooks/html/curse_of_dimensionality.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/curse_of_dimensionality.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/curse_of_dimensionality_standalone.ipynb) |
| (13) Data Batching for Training LLMs[HTML](notebooks/html/llm_training_data_preparation_batching.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/llm_training_data_preparation_batching.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/llm_training_data_preparation_batching_standalone.ipynb) |
| (14) Data Normalization — Motivation & Overview[HTML](notebooks/html/data_normalization_overview.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/data_normalization_overview.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/data_normalization_overview_standalone.ipynb) |
| (15) Data Preparation for Training LLMs — An Overview[HTML](notebooks/html/llm_training_data_preparation_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/llm_training_data_preparation_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/llm_training_data_preparation_basics_standalone.ipynb) |
| (16) Decision Trees[HTML](notebooks/html/decision_trees_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/decision_trees_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/decision_trees_basics_standalone.ipynb) |
| (17) Decision Trees — CART (Classification and Regression Trees)[HTML](notebooks/html/decision_trees_cart.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/decision_trees_cart.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/decision_trees_cart_standalone.ipynb) |
| (18) Dropout[HTML](notebooks/html/nn_dropout.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/nn_dropout.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/nn_dropout_standalone.ipynb) |
| (19) Gradient Descent with Momentum[HTML](notebooks/html/gradient_descent_momentum.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/gradient_descent_momentum.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/gradient_descent_momentum_standalone.ipynb) |
| (20) Gradient Descent — The (Very) Basics[HTML](notebooks/html/gradient_descent_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/gradient_descent_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/gradient_descent_basics_standalone.ipynb) |
| (21) Handwritten Digit Recognition with Artificial Neural Networks (ANNs)[HTML](notebooks/html/handwritten_digit_recognition_ann.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/handwritten_digit_recognition_ann.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/handwritten_digit_recognition_ann_standalone.ipynb) |
| (22) Implementing an ANN from Scratch (NumPy only)[HTML](notebooks/html/ann_from_scratch_numpy_only.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/ann_from_scratch_numpy_only.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/ann_from_scratch_numpy_only_standalone.ipynb) |
| (23) Language Models[HTML](notebooks/html/language_models_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/language_models_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/language_models_basics_standalone.ipynb) |
| (24) Linear Regression[HTML](notebooks/html/linear_regression_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/linear_regression_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/linear_regression_basics_standalone.ipynb) |
| (25) Linear Regression — Assumptions & Caveats[HTML](notebooks/html/linear_regression_assumptions_caveats.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/linear_regression_assumptions_caveats.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/linear_regression_assumptions_caveats_standalone.ipynb) |
| (26) LoRA Fine-Tuning — A Basic Example[HTML](notebooks/html/llm_model_finetuning_lora_hf_kidsqa.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/llm_model_finetuning_lora_hf_kidsqa.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/llm_model_finetuning_lora_hf_kidsqa_standalone.ipynb) |
| (27) Logistic Regression — Basics[HTML](notebooks/html/logistic_regression_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/logistic_regression_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/logistic_regression_basics_standalone.ipynb) |
| (28) Logistic Regression: The Math[HTML](notebooks/html/logistic_regression_math.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/logistic_regression_math.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/logistic_regression_math_standalone.ipynb) |
| (29) Logit Distillation[HTML](notebooks/html/knowledge_distillation_logit_distillation.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/knowledge_distillation_logit_distillation.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/knowledge_distillation_logit_distillation_standalone.ipynb) |
| (30) Machine Translation with Transformers[HTML](notebooks/html/machine_translation_transformers.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/machine_translation_transformers.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/machine_translation_transformers_standalone.ipynb) |
| (31) Masking in Sequence Models[HTML](notebooks/html/masking_sequence_models.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/masking_sequence_models.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/masking_sequence_models_standalone.ipynb) |
| (32) Mixture of Experts (MoE)[HTML](notebooks/html/mixture_of_experts_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/mixture_of_experts_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/mixture_of_experts_basics_standalone.ipynb) |
| (33) Model Fine-Tuning for LLMs — An Overview[HTML](notebooks/html/llm_model_fine_tuning_overview.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/llm_model_fine_tuning_overview.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/llm_model_fine_tuning_overview_standalone.ipynb) |
| (34) Multinomial Naive Bayes (Basics)[HTML](notebooks/html/multinomial_naive_bayes_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/multinomial_naive_bayes_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/multinomial_naive_bayes_basics_standalone.ipynb) |
| (35) NumPy — Basic Tutorial[HTML](notebooks/html/numpy_basic_tutorial.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/numpy_basic_tutorial.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/numpy_basic_tutorial_standalone.ipynb) |
| (36) Part-of-Speech (POS) Tagging (Basics)[HTML](notebooks/html/part_of_speech_tagging_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/part_of_speech_tagging_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/part_of_speech_tagging_basics_standalone.ipynb) |
| (37) Porter Stemmer[HTML](notebooks/html/porter_stemmer.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/porter_stemmer.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/porter_stemmer_standalone.ipynb) |
| (38) Positional Encodings — Overview[HTML](notebooks/html/positional_encodings_overview.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/positional_encodings_overview.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/positional_encodings_overview_standalone.ipynb) |
| (39) RNN-based Language Models[HTML](notebooks/html/recurrent_neural_networks_language_model.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/recurrent_neural_networks_language_model.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/recurrent_neural_networks_language_model_standalone.ipynb) |
| (40) Recurrent Neural Networks — An Introduction[HTML](notebooks/html/recurrent_neural_networks_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/recurrent_neural_networks_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/recurrent_neural_networks_basics_standalone.ipynb) |
| (41) Resource-Efficient LLMs — An Overview[HTML](notebooks/html/llm_resource_efficiency_overview.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/llm_resource_efficiency_overview.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/llm_resource_efficiency_overview_standalone.ipynb) |
| (42) Retrieval-Augmented Generation (RAG) — A (Very) Basic Example[HTML](notebooks/html/retrieval_augmented_generation_rag_basic_example.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/retrieval_augmented_generation_rag_basic_example.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/retrieval_augmented_generation_rag_basic_example_standalone.ipynb) |
| (43) Retrieval-Augmented Generation (RAG) — Basics[HTML](notebooks/html/retrieval_augmented_generation_rag_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/retrieval_augmented_generation_rag_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/retrieval_augmented_generation_rag_basics_standalone.ipynb) |
| (44) Rotary Position Embeddings (RoPE)[HTML](notebooks/html/positional_encodings_rope_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/positional_encodings_rope_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/positional_encodings_rope_basics_standalone.ipynb) |
| (45) Sinusoidal Positional Encodings (Original Transformer)[HTML](notebooks/html/positional_encodings_original_transformer.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/positional_encodings_original_transformer.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/positional_encodings_original_transformer_standalone.ipynb) |
| (46) Stemming & Lemmatization[HTML](notebooks/html/stemming_lemmatization_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/stemming_lemmatization_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/stemming_lemmatization_basics_standalone.ipynb) |
| (47) Subword Tokenization (WordPiece)[HTML](notebooks/html/wordpiece_tokenization.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/wordpiece_tokenization.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/wordpiece_tokenization_standalone.ipynb) |
| (48) Text Classification with Recurrent Neural Networks (RNNs)[HTML](notebooks/html/text_classification_rnn.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/text_classification_rnn.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/text_classification_rnn_standalone.ipynb) |
| (49) Text Normalization[HTML](notebooks/html/text_normalization_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/text_normalization_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/text_normalization_basics_standalone.ipynb) |
| (50) Text Tokenization[HTML](notebooks/html/text_tokenization_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/text_tokenization_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/text_tokenization_basics_standalone.ipynb) |
| (51) The AdaGrad Optimizer[HTML](notebooks/html/adagrad_optimizer.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/adagrad_optimizer.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/adagrad_optimizer_standalone.ipynb) |
| (52) The Adam Optimizer[HTML](notebooks/html/adam_optimizer.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/adam_optimizer.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/adam_optimizer_standalone.ipynb) |
| (53) The Linear Layer[HTML](notebooks/html/nn_linear_layer.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/nn_linear_layer.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/nn_linear_layer_standalone.ipynb) |
| (54) The Math Behind Linear Regression[HTML](notebooks/html/linear_regression_math.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/linear_regression_math.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/linear_regression_math_standalone.ipynb) |
| (55) The RMSProp Optimizer[HTML](notebooks/html/rmsprop_optimizer.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/rmsprop_optimizer.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/rmsprop_optimizer_standalone.ipynb) |
| (56) The Softmax Function[HTML](notebooks/html/nn_softmax.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/nn_softmax.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/nn_softmax_standalone.ipynb) |
| (57) Token Indexing with Vocabularies[HTML](notebooks/html/text_token_indexing.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/text_token_indexing.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/text_token_indexing_standalone.ipynb) |
| (58) Training Word2Vec from Scratch[HTML](notebooks/html/word2vec_training_from_scratch.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/word2vec_training_from_scratch.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/word2vec_training_from_scratch_standalone.ipynb) |
| (59) Transformers — Basic Architecture[HTML](notebooks/html/transformers_basic_architecture.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/transformers_basic_architecture.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/transformers_basic_architecture_standalone.ipynb) |
| (60) Using Pretrained LLMs Locally — A Starter Guide[HTML](notebooks/html/llm_local_inference_pretrained_models.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/llm_local_inference_pretrained_models.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/llm_local_inference_pretrained_models_standalone.ipynb) |
| (61) Vector Space Model[HTML](notebooks/html/vector_space_model_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/vector_space_model_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/vector_space_model_basics_standalone.ipynb) |
| (62) Word & Text Embeddings — An Overview[HTML](notebooks/html/word_text_embeddings_overview.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/word_text_embeddings_overview.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/word_text_embeddings_overview_standalone.ipynb) |
| (63) Working with Batches for Sequence Tasks[HTML](notebooks/html/batch_processing_sequence_tasks.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/batch_processing_sequence_tasks.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/batch_processing_sequence_tasks_standalone.ipynb) |
| (64) Working with the OpenAI API — An Introduction[HTML](notebooks/html/llm_openai_api_basics.html)[GitHub](https://github.com/chrisvdweth/selene/blob/master/notebooks/llm_openai_api_basics.ipynb)[Colab](https://githubtocolab.com/chrisvdweth/selene/blob/master/notebooks/standalone/llm_openai_api_basics_standalone.ipynb) |
"""

# Regex now just captures the raw URL strings from the block
pattern = r'\|\s*\(\d+\)\s*(.*?)(?:\[HTML\]\((.*?)\))(?:\[GitHub\]\((.*?)\))(?:\[Colab\]\((.*?)\))\s*\|'
matches = re.findall(pattern, raw_text)

notebooks = {}
for match in matches:
    title = match[0].strip()
    
    # 1. Process HTML Path
    raw_html = match[1].strip()
    # Handle both relative paths ("notebooks/html/...") and absolute paths in the raw text
    if raw_html.startswith('http'):
        html_path = raw_html.split("selene/")[-1] 
    else:
        html_path = raw_html
    # Use f-string to build final URL
    html_url = f"{PAGES_BASE_URL}/{html_path}"
        
    # 2. Process GitHub Path
    # Split on "master/" to extract just "notebooks/name.ipynb"
    github_path = match[2].strip().split("master/")[-1]
    github_url = f"{GITHUB_BASE_URL}/{github_path}"
    
    # 3. Process Colab Path
    colab_path = match[3].strip().split("master/")[-1]
    colab_url = f"{COLAB_BASE_URL}/{colab_path}"
    
    notebooks[title] = {"HTML": html_url, "GitHub": github_url, "Colab": colab_url}

phases = {
    "Phase 1: Foundations & Classical Machine Learning": [
        "NumPy — Basic Tutorial",
        "Data Normalization — Motivation & Overview",
        "Curse of Dimensionality",
        "Linear Regression",
        "Linear Regression — Assumptions & Caveats",
        "The Math Behind Linear Regression",
        "Logistic Regression — Basics",
        "Logistic Regression: The Math",
        "Gradient Descent — The (Very) Basics",
        "Decision Trees",
        "Decision Trees — CART (Classification and Regression Trees)",
        "Multinomial Naive Bayes (Basics)",
        "Bias & Variance (Machine Learning)",
        "Bias-Variance Decomposition"
    ],
    "Phase 2: Deep Learning Foundations (Neural Networks)": [
        "Artificial Neural Networks (Basic Architecture)",
        "The Linear Layer",
        "Activation Functions",
        "The Softmax Function",
        "Dropout",
        "Backpropagation",
        "Backpropagation (Generalization)",
        "Implementing an ANN from Scratch (NumPy only)",
        "Gradient Descent with Momentum",
        "The AdaGrad Optimizer",
        "The RMSProp Optimizer",
        "The Adam Optimizer",
        "Handwritten Digit Recognition with Artificial Neural Networks (ANNs)"
    ],
    "Phase 3: Classical Natural Language Processing (NLP)": [
        "Text Normalization",
        "Stemming & Lemmatization",
        "Porter Stemmer",
        "Part-of-Speech (POS) Tagging (Basics)",
        "Text Tokenization",
        "Token Indexing with Vocabularies",
        "Building a Word Tokenizer from Scratch",
        "Subword Tokenization (WordPiece)",
        "Byte-Pair Encoding Tokenization",
        "Vector Space Model",
        "Word & Text Embeddings — An Overview",
        "Training Word2Vec from Scratch"
    ],
    "Phase 4: Sequence Models & Recurrent Neural Networks (RNNs)": [
        "Recurrent Neural Networks — An Introduction",
        "Backpropagation Through Time (BPTT)",
        "Working with Batches for Sequence Tasks",
        "Masking in Sequence Models",
        "Language Models",
        "RNN-based Language Models",
        "Text Classification with Recurrent Neural Networks (RNNs)"
    ],
    "Phase 5: The Transformer Revolution": [
        "Attention & Multi-Head Attention",
        "Positional Encodings — Overview",
        "Sinusoidal Positional Encodings (Original Transformer)",
        "Rotary Position Embeddings (RoPE)",
        "Transformers — Basic Architecture",
        "Machine Translation with Transformers"
    ],
    "Phase 6: Large Language Models (LLMs) & Advanced AI": [
        "Data Preparation for Training LLMs — An Overview",
        "Data Batching for Training LLMs",
        "Building a GPT-Style LLM from Scratch",
        "Mixture of Experts (MoE)",
        "Model Fine-Tuning for LLMs — An Overview",
        "LoRA Fine-Tuning — A Basic Example",
        "Logit Distillation",
        "Retrieval-Augmented Generation (RAG) — Basics",
        "Retrieval-Augmented Generation (RAG) — A (Very) Basic Example",
        "Resource-Efficient LLMs — An Overview",
        "Using Pretrained LLMs Locally — A Starter Guide",
        "Working with the OpenAI API — An Introduction"
    ]
}

# Template the markdown header as well
markdown_content = f"# Selene: Curated Learning Path\n\nThis document outlines a structured, progressive learning path through the [Selene repository]({PAGES_BASE_URL}) notebooks.\n\n"

for phase_name, topics in phases.items():
    markdown_content += f"## {phase_name}\n\n"
    markdown_content += "| Topic | Web | Source | Interactive |\n"
    markdown_content += "|---|---|---|---|\n"
    for topic in topics:
        if topic in notebooks:
            data = notebooks[topic]
            markdown_content += f"| {topic} | [HTML]({data['HTML']}) | [GitHub]({data['GitHub']}) | [Colab]({data['Colab']}) |\n"
        else:
            markdown_content += f"| {topic} | - | - | - |\n"
    markdown_content += "\n"

with open("selene_curated_path.md", "w") as f:
    f.write(markdown_content)

print("Markdown generated with clean URL templating")
