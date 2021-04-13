CREATE TABLE Teams (
  team_id INT ,
  team_name VARCHAR (20)
) ;

CREATE TABLE Matches (
  match_id INT ,
  host_team INT ,
  guest_team INT ,
  host_goals  INT,
  guest_goals INT
) ;

INSERT INTO Teams (team_id, team_name) 
VALUES
  (10, 'Leetcode FC') ;
  
INSERT INTO Teams (team_id, team_name) 
VALUES
  (20, 'NewYork FC') ;

INSERT INTO Teams (team_id, team_name) 
VALUES
  (30, 'Atlanta FC') ;
  
INSERT INTO Teams (team_id, team_name) 
VALUES
  (40, 'Chicago FC') ;
  
INSERT INTO Teams (team_id, team_name) 
VALUES
  (50, 'Toronto FC') ;

INSERT INTO Matches (
  match_id,
  host_team,
  guest_team,
  host_goals,
  guest_goals
) 
VALUES
  (1, 10, 20, 3, 0) ;

INSERT INTO Matches (
  match_id,
  host_team,
  guest_team,
  host_goals,
  guest_goals
) 
VALUES
  (2, 30, 10, 2, 2) ;

INSERT INTO Matches (
  match_id,
  host_team,
  guest_team,
  host_goals,
  guest_goals
) 
VALUES
  (3, 10, 50, 5, 1) ;
  
INSERT INTO Matches (
  match_id,
  host_team,
  guest_team,
  host_goals,
  guest_goals
) 
VALUES
  (4, 20, 30, 1, 0) ;
  
INSERT INTO Matches (
  match_id,
  host_team,
  guest_team,
  host_goals,
  guest_goals
) 
VALUES
  (5, 50, 30, 1, 0) ;

select Teams.team_id, Teams.team_name, 
    sum(case when team_id=host_team and host_goals>guest_goals then 3 else 0 end) +
    sum(case when team_id=host_team and host_goals=guest_goals then 1 else 0 end) +
    sum(case when team_id=guest_team and host_goals<guest_goals then 3 else 0 end) +
    sum(case when team_id=guest_team and host_goals=guest_goals then 1 else 0 end) as num_points
from Teams left join Matches
on Teams.team_id = Matches.host_team or Teams.team_id = Matches.guest_team
group by Teams.team_id,Teams.team_name
order by num_points desc, Teams.team_id asc
