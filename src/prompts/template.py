from langchain.prompts import PromptTemplate

mcq_prompt_template = PromptTemplate(
    template=(
        "You are a briliant study question generator. I'll give you $50 to create ONE multiple-choice question.\n\n"
        "Requirements:\n"
        "1. The question must be about the topic: {topic}.\n"
        "2. Difficulty level: {difficulty}.\n"
        "3. Provide EXACTLY 4 unique answer options.\n"
        "4. Ensure that only ONE option is correct.\n"
        "5. The 'correct_answer' MUST be one of the options listed.\n"
        "6. Return ONLY a valid JSON object with no explanations, no extra text, and no markdown formatting.\n"
        "7. Ensure the JSON is valid and properly formatted.\n\n"
        "Return ONLY a JSON object with this exact structure:\n"
        "{{\n"
        '    "question": "<clear and specific question>",\n'
        '    "option": ["<option1>", "<option2>", "<option3>", "<option4>"],\n'
        '    "correct_answer": "<exactly one of the options above>"\n'
        "}}\n\n"
        "Example:\n"
        "{{\n"
        '    "question": "What is the capital of Japan?",\n'
        '    "option": ["Seoul", "Tokyo", "Beijing", "Bangkok"],\n'
        '    "correct_answer": "Tokyo"\n'
        "}}\n\n"
        "Your response:"
    ),
    input_variables=["topic", "difficulty"]
)

maq_prompt_template = PromptTemplate(
    template=(
        "You are a brilliant study question generator. I'll give you $50 to create ONE multiple-answer question.\n\n"
        "Requirements:\n"
        "1. The question must be about the topic: {topic}.\n"
        "2. Difficulty level: {difficulty}.\n"
        "3. Provide EXACTLY 5 unique answer options.\n"
        "4. The number of correct answers can range from 1 to 5.\n"
        "5. 'correct_answers' MUST be a list containing ONLY items that appear in 'options'.\n"
        "6. Return ONLY a valid JSON object with no explanations, no extra text, and no markdown formatting.\n"
        "7. Ensure the JSON is valid and properly formatted.\n\n"
        "Return ONLY a JSON object with this exact structure:\n"
        "{{\n"
        '    "question": "<clear and specific question>",\n'
        '    "option": ["<option1>", "<option2>", "<option3>", "<option4>", "<option5>"],\n'
        '    "correct_answer": ["<one or more correct options from above>"]\n'
        "}}\n\n"
        "Example:\n"
        "{{\n"
        '    "question": "Which of the following are programming languages?",\n'
        '    "option": ["Python", "HTML", "Java", "C++", "CSS"],\n'
        '    "correct_answer": ["Python", "Java", "C++"]\n'
        "}}\n\n"
        "Your response:"
    ),
    input_variables=["topic", "difficulty"]
)

fill_blank_prompt_template = PromptTemplate(
    template=(
        "You are a brilliant study question generator. I'll give you $50 to create ONE fill-in-the-blank question.\n\n"
        "Requirements:\n"
        "1. The question must be about the topic: {topic}.\n"
        "2. Difficulty level: {difficulty}.\n"
        "3. The 'question' MUST contain exactly one blank represented by '_____'.\n"
        "4. The 'answer' must be the correct word or phrase that fills the blank.\n"
        "5. Return ONLY a valid JSON object with no explanations, no extra text, and no markdown formatting.\n"
        "6. Ensure the JSON is valid and properly formatted.\n\n"
        "Return ONLY a JSON object with this exact structure:\n"
        "{{\n"
        '    "question": "<sentence with exactly one _____>",\n'
        '    "correct_answer": "<correct word or phrase>"\n'
        "}}\n\n"
        "Example:\n"
        "{{\n"
        '    "question": "The chemical symbol for water is _____.",\n'
        '    "correct_answer": "H2O"\n'
        "}}\n\n"
        "Your response:"
    ),
    input_variables=["topic", "difficulty"]
)