from difflib import get_close_matches
"""use to compare a list and a string
going to find a best match"""

def get_best_match(user_question: str, questions: dict) -> str | None:
    """return None if chance no answer to what we looking for"""
    questions: list[str] = [q for q in questions]
    """create variable matches that will provide a list"""
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    """comparing user question to the list of questions
    specify only want to return the best one
    can return multiple but one for now
    cutoff parameter to 60% why?
    60% match at least to user 
    to give a valid response"""

    if matches:
        return matches[0]
    """if there is a match -> return a match of the first match"""

def chat_bot(knowledge: dict):
    while True:
        user_input: str = input('You: ')
        best_match: str | None = get_best_match(user_input, knowledge)

        if answer := knowledge.get(best_match):
            """this gonna return us a question formatted correctly
            so we can use it as key for knowledge dot get"""
            print(f'Bot: {answer}')
            """if there is an answer print answer or
            else bot has no idea what we talking bout"""
        else:
            print('Bot: I do not understand...')

if __name__ == '__main__':
    brain: dict = {'hello': 'Hey there!',
                   'how are you': 'I am good, thanks!',
                   'what time is it': 'Don\'t know, don\'t care...',
                   'bye': 'See you!'
                   }

chat_bot(knowledge=brain)
