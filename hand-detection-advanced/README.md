`This submission for hackathon as the name suggests is a hack.`

## Functions
1. Used open-cv to read the video
2. mediapipe to detect if hand is there is the frame
3. Logic for false negative in hand tracking
4. building a dictionary of information
5. Finding the information which matches the question the most.
6. forming the answer
7. rephrasing the answer

The rules of the hackathon suggest that the answers shouldn't be preset. This solution sits on the thin line of having/not having preset answers.

Since there can be only so many questions that can be asked about a video, we can fix the set of questions(in a pragmatic sense). The model is capable of extracting only information like `how many times the hand was raise?`. We can exploit this simplicity by predefining a set of questions. Any question that the user enters will be checked for similarity against this set of questions. We use cosine similarity to achieve this. The answer is also preset(kind of), we can give out differently framed answers to the same question because we paraphrase the answer, which means the answer is not preset. This is more efficient that training a language model to answer a question beased on some information(like you tell the model that the hand was raised 5 times)

## Other considerations.
It is possible for mediapipe handtracking to give out false negatives. The assumption is that it will be able to correct it's output withing 1 sec. (30 frames in test video). If the handtracking model says there is no hand at t seconds, but before t+1 seconds it says there is a hand, then we would consider that hand not being there was a false negative.

## Is Cosine similarity good way to compare sentences
Consider the following examples
1. The cat climbed a tall tree.
2. The tree climbed a tall cat.

The second sentence is absurd, but it sure conveys a different meaning from the first sentence. The cosine similarity of these two sentences is 1.
That being said, for the particular questions that we have in this hackathon, cosine similarity is good enough.
