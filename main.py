from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain_core.output_parsers import PydanticOutputParser
from schemas import ResumeData
from dotenv import load_dotenv
from utils import extract_text

load_dotenv()


def load_chain() -> Runnable:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash")
    parser = PydanticOutputParser(pydantic_object=ResumeData)
    template = PromptTemplate(
        template="""
                You are a resume parser. Extract the following fields from the given resume text and return in JSON format:

            - Full Name
            - Email
            - Phone
            - Summary
            - Education (degree, institution, year)
            - Work Experience (company, title, duration, description)
            - Skills
            - Projects
            - Certifications

            Resume Text:
            -----------------
            {resume_text}
            -----------------
            Output JSON:
            {format_instruction}
        """,
        input_variables=['resume_text'],
        partial_variables={"format_instruction": parser.get_format_instructions()})
    return template | llm | parser


def parse_resume(file_path: str) -> ResumeData:
    resume_text = extract_text(file_path)
    chain = load_chain()
    response = chain.invoke({"resume_text": resume_text})
    return response


if __name__ == "__main__":
    result = parse_resume("sample_resume.pdf")
    print(result, result.name)
