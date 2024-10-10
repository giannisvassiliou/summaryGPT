# summaryGPT 

Semantic summaries try to extract compact information from
 the original knowledge graph (KG) while reducing its size for various pur
poses such as query answering, indexing, or visualization. Although so
 far several techniques have been exploited for summarizing individual
 KGs, to the best of our knowledge, there is no approach summarizing
 the interests of the users in exploring those KGs, capturing also how
 these evolve. SummaryGPT fills this gap by enabling the exploration of
 users’ interests as captured from their queries over time. For generat
ing these summaries we first extract the nodes appearing in query logs,
 captured from a specific time period, and then we classify them into
 different categories in order to generate quotient summaries on top. For
 the classification, we explore both the KG type hierarchy (if existing)
 and also a large language model, i.e. ChatGPT. Exploring different time
 periods enables us to identify shifts in user interests and capture their
 evolution through time. In this demonstration we use WikiData KG in
 order to enable active exploration of the corresponding user interests,
 allowing end-users to visualize how these evolve over time



#In code folder the .py file opens the seven out*.txt files with labels, and with the help of GPT translates them to categories (topics)

# the api key should be updated and also since openAI changed its API some functions are outdated and maybe should re-written
