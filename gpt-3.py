import openai


def gpt3(stext):
    openai.api_key = 'JpRSimgQzVbDFX440JlvT3BlbkFJmMujtIBLCZidWdhQF7n0'
    response = openai.Completion.create(
        engine="davinci-instruct-beta",

    )
