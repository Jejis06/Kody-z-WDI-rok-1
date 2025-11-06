import ast
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
class gptGen:
    def __getattr__(self, name):
        # generate code for function definition with google gemini

        code_string = ""
        try:
            tree = ast.parse(code_string)
            func_node = next(node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
            func_name = func_node.name
        except (StopIteration, SyntaxError) as e:
            raise ValueError(f"Could not find a function definition in the string. Error: {e}")
        namespace = {}
        try:
            exec(code_string, {}, namespace)
        except Exception as e:
            print(f"Error executing string: {e}")
            return None
        return namespace.get(func_name)

gpt = gptGen()
x = 10
sqrt = gpt.sqrt
print(sqrt(x))