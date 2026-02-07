import google.generativeai as genai

genai.configure(api_key="AIzaSyDmHjNgUXCAoszymU3SHrb2wNAYG4k3bJE")

models = genai.list_models()
for m in models:
    print(m.name, "->", m.supported_generation_methods)
