from src.user import User
from src.user_list import UserList
from login import sign_in



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    user_list = UserList()

    user = User("user_01", "123mudar")
    user_list.add_user(user)

    sign_in(user_list)



    #
    # load_dotenv()
    #
    # client = OpenAI()
    #
    # role_file_path = "role.txt"
    # role = read_text_file(role_file_path)
    #
    # instruction_file_path = "instruction.txt"
    # instruction = read_text_file(instruction_file_path)
    #
    # example_file_path = "example.txt"
    # example = read_text_file(example_file_path)
    #
    # symptoms = "Estou sentindo uma dor forte ao urinar há 3 dias. Tenho também casos de febre"
    #
    # question = llm.generate_question(instruction, symptoms, example)
    #
    # answer = llm.generate_answer(client, role, question)
    # print(answer)
