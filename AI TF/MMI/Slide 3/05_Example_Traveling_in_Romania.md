# 🇷🇴 Example: Traveling in Romania

**Problem:** Travel from Arad to Bucharest.

|Component|Formulation|Details|
|---|---|---|
|**Goal**|Be in Bucharest.|Satisfies the Goal Test.|
|**States**|Various cities (e.g., Arad, Sibiu, Pitesti).|The discrete situations.|
|**Initial State**|Arad.|The starting city.|
|**Actions/Operators**|Drive between connected cities.|Legal moves based on the road network.|
|**Path Cost**|Sum of distances.|The step cost is the road distance (e.g., Arad-Sibiu is 140).|
|**Solution**|A sequence of cities (e.g., Arad $\to$ Sibiu $\to$ Fagaras $\to$ Bucharest).|The path that minimizes the path cost.|