# Low Level Design of Cricbuzz

'''
1. Requirements Gathering
    a. Multiple Ongoing matches
    b. Each match has own scorecard
    c. Scorecard gets updated ball by ball
    d. Scorecard should contain all details about Innings, Batsmen stats and Bowler stats.

2. Flow
    Two teams ---> Single Match ---> Innings 1 ---> Team A Bats  ---> 11 Players ---> Scores
                                                    Team B Bowls ---> 11 Players ---> Scores
                                ---> Innings 2 ---> Team B Bats  ---> 11 Players ---> Scores
                                                    Team A Bowls ---> 11 Players ---> Scores

3. Possible Objects
    a. Match          
    b. Team
    c. Players
    d. Innings
    e. Scorecard
    f. Additional objects can be - Overs, Balls, Pitches, etc.

4. Relationships
    a. Match
        i. Team teamA
        ii. Team teamB
        iii. Date date
        iv. String Venue
        v. Matchtype type
        vi. Innings inning
        vii. Team tosswinner
'''
