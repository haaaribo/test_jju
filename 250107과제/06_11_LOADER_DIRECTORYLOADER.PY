from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("C:\\Users\\SANGMIN\\OneDrive\\문서\\GitHub\\test_jju\\250107과제\\data_all", glob="**/*.md")

docs = loader.load()

print(len(docs))
# print(docs[0].page_content[:100])
