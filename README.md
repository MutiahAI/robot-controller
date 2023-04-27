### ROS package that automatically generates point-to-point cubic trajectories connecting pairs of randomly generated points. 
##### After running the launch file, random trajectories can be seen appearing on the rqt_plot GUI (i.e. a different set of trajectories every 20 seconds).

### To run the package:

1.) Download the attached package into your catkin workspace,

2.) Run the 'source /opt/ros/noetic/setup.bash'and '. ~/catkin_ws1/devel/setup.bash' command from the now opened catkin workspace. Take note to do this for every newly opened terminal

3.) Run the 'catkin_make' command from the same workspace

4.) Run the 'roscore'command from a new terminal,

5.) Once the workspace is ready, make all the nodes executable by running the commands below from the "scripts" folder containing all the nodes in the terminal where 'catkin_make' command was run:

  'chmod +x plot_cubic_traj.py
   chmod +x points_generator.py
   chmod +x compute_cubic_coeffs.py
   chmod +x plot_cubic_traj.py'

6.) Launch the package by running:

  'roslaunch ar_week5_test cubic_traj_gen.launch'

7.) After about 20 seconds, Run 'rqt_graph' in a new terminal to get the visual representation of the package

### List of Dependencies:

- python 3.8.10
- ros-noetic
- Numpy
