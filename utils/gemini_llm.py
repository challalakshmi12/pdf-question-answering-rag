from config import gemini_model


def generate_answer(prompt):

    print("\n" + "=" * 60)
    print("STEP 8 : GEMINI GENERATING ANSWER")
    print("=" * 60)

    response = gemini_model.generate_content(prompt)

    print("\nGemini Response\n")

    print(response.text)

    return response.text