# RuleEngine

# Discussion Questions:
Q1. Briefly describe the conceptual approach you chose! What are the trade-offs? A. I have created APIs for performing CRUD(Create, Retrieve, Update, Delete) operations on rules. There is a sepearte API provided for filtering data which takes Rule Ids and filter the data which violates the rule. Trade off is instead of having normalised database(Keeping seperate table for storing operations), I decided to keep opeartions in the same table as rules, so that extra database call will be saved.

Q2. What's the runtime performance? What is the complexity? Where are the bottlenecks?
A. For the sample data(raw_signal.json) provided in the question, the latency is 30- 50ms with three rules applied. The complexity is O(N) where N is the number of rows of data.The major bottleneck I faced is defining the unified operations for all the value types.

Q3.If you had more time, what improvements would you make, and in what order of priority?
A. Firstly, I would have liked to introduce the cache service to it so that all the old rules will be stored in cache and DB calls will be made only for new rules. Next I would introduce a script for taking the latest code from Github and building a Docker image using Jenkins so that deployment will be fast.
