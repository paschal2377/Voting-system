#nominating two greatest football players of all time
nominee1 = "Lionel Messi"
nominee2 = "Cristiano Ronaldo"
# intial vote count for two of the greatest players ever
nom1_votes = 0
nom2_votes = 0

voters_id = [ 13444,15611,17843,19824,16812,10234,12324,23771,23725,23562]

no_of_voters = len(voters_id)

while True:
    if voters_id == [] : # checking when voters id are all used
        print("All eligible fans have voted!!!")
        if nom1_votes > nom2_votes :
            percent = (nom1_votes/no_of_voters) * 100
            print(nominee1,"is the greatest player of all time!")
            print("He won the election with",percent,"%")
            break # get rid of infinite loop
        elif nom2_votes > nom1_votes :
            percent = (nom2_votes/no_of_voters)*100
            print(nominee2,"is the greatest player of all time!")
            print("He won the election with",percent,"%")
            break
        else:
            print("Oh! equal votes!!")
            break
    
    voter = int(input("Enter your Id number to vote:"))
    if voter in voters_id:
        print("You are eligible to vote")
        voters_id.remove(voter) # so that same vote can't vote again
        print("-------------------------------------")
        print("To give vote to",nominee1,"Press 1 ")
        print("To give vote to",nominee2,"Press 2")
        print("-------------------------------------")
        vote = int(input("Who is the goat?"))
        if vote == 1:
            nom1_votes += 1
            print(nominee1,"You have chosen your favourite player!!")
        elif vote > 2 :
            print("Please! kindly check Press keys!")
        else :
            print("You are ineligible to vote")




