"""
    This is a program that will show you resume matching based on cosine similarity
    The highest the returned value is the more chances to get hired

    @Constantin Irimia

"""

# First lets import the libraries
# If using a virtual environment just type in terminal: pip install docx2txt
import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Here is the resume that you want to process
resume = docx2txt.process("yourResume.docx")

# Here is the job description
job_description = docx2txt.process("job_description.docx")

# Put these variables into list
text = [resume, job_description]

# Create the model and train it
countVectorizer = CountVectorizer()
count_matrix = countVectorizer.fit_transform(text)


# Print the similarity scores
print("-------------------------------------------------")
print("Similarity Scores using cosine similarity: ")
print(cosine_similarity(count_matrix))

# Print the matching in percentage
matching = cosine_similarity(count_matrix)[0][1] * 100
print("-------------------------------------------------")
print("")
print("This resume matches " + str(round(matching, 3)) + "% of the job description.")
