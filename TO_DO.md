Main function:
    - Add function that plots the state of the cars. We should probably have a list of all active objects for this function. It      should also convert the coordinates of each car to a position in a discrete matrix that can be plotted.
   
lane.py:
    - Create 2 subclasses, one for intersections and one for roads.

    Intersections:
        - Add parametric equation that cars will fetch when they use the lane
        - Should collision detection for turns be checked for the lane instead of the car?
        - Perhaps useful some functionality for making all the lanes for an entire intersection quickly (how to make
          the parametric equations quickly?)
        - Link active lanes to configurations from intersectionConfigs.py
        - Perhaps collision detection can be done using the parametric equations instead of the vision field of the car?
        - Function that makes pedestrians able to cross road.
        - Link intersections to traffic lights or possibly remove traffic lights if found to be unnecessary
        - What do we want yellow lights to do?
 
    Roads:
        - Add functionality for swapping lanes
        - Use a queue to store the order of the cars in the lanes
        - Add function that cars can call to learn distance to next intersection

light.py
    - Is this file necessary? Might be easier to just have 16 (or fewer depending on intersection) intersection
      lanes, and having some be active and others be inactive.