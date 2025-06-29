# System Design Interview Framework

"提出好问题的能力也是一项重要的技能，许多面试官特别看重这项技能。"
"The ability to ask good question is an import skill that many interviewers look for.

## 4 Steps

### 1 Step: understand the question and make sure what's need to be designed

* How many users in this software
* What's the specific function need to be develop in this produce
* What's the company's technology stack?
* Mobile app or Web system or both of them?
* Which one is the most important function?
* Some Detail question for the project (different project will have different question). you need understand the question at first.

### 2. Step: Give the High level Design and get Agreement

* give a generate design and ask the interviewer for the agreement
* draw the block diagram fo the key components, include client, API, Network , storage, cache, CDN, Message Queue, etc.
* make a generate data assessment for this system, and communicate with your interviewer

you can give some use case, to discuss with interviewer. It helps to get more info I ignored.

If the question is not very hight level such as Google Search engine, or ChatGPT product. There must have special data struct need to be clarify.

### 3 Step: Deep Dive

* make sure the most important function or part of this system with interview
* Don't discuss with interview about the specific method to implement the module or function. This will waste time, You need just give a general description about that, if the interview ask the detail, then give him the detail description
* give a better the summary about the whole system

### 4. Summary about your design

* sometime interviewer need you find some bottleneck of this system you designed. Give the honest answer don't think your system is perfect. give him that your opinion what need to be improved. 
* Error Condition : Server down, Network package loss etc. need to be discuss

## What Should Do and Shouldn't Do

Should Do:

* make clear of the question, don't assume that you are clear all about that.
* understand the requirement
* Let interviewer knows what you are thinking about. Discuss with interviewer all the time.
* Provide multi solution if you can and explain the better or worse of each way.
* make a agreement with your interview and make detail design. Start from the most important part.
* Don't give up!!!

Shouldn't Do

* Without any preparation with typical question
* Give solution without clear all the requirement and assumption.
* Don't make deep analysis for one part at beginning. Give the general design at first.
* Ask for promotion if you are stuck.
* Keep communicating, don't be quiet.
* Don't think you finished your design, the interview is ended until the interviewer says it's ended, that's it.

## Time distribute for each step

The total time of one interview always be 45 mins:

* Understand the question and make sure what's the target need to be design: 3~10 mins
* Give a high level design or general design and make sure you got agreement. 10~15 mins
* Deep dive  10~25 mins
* Summary of whole system design. 3~5 mins

