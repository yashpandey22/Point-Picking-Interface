# Point-Picking-Interface
This python interface allows the selection of points from a point cloud and transfers them as keyboard inputs to Floradig software for digitization purposes.

# Software Requirements
  1. Floradig installed and working, with a "ini" file.
  2. Python version 3.7 is required to run the script.
     Download Python: https://www.python.org/downloads/release/python-370/
  3. Install following libraries, enter the following command in the cmd: 
     ```
     pip install open3d
     pip install pywin32
     
     ```

# How to use the interface
  ## Step 1:
   1. Execute Floradig software.
   2. Select digitiser to "Keyboard Digitiser"
      Digitiser -> Select Digitiser (Alt+Z) -> Keyboard mock digitiser -> Set as current -> Ok.
      
      |![1](https://user-images.githubusercontent.com/42251021/220800033-d39b2ba7-2fb5-413d-b2a5-154d79ef150e.png) | 
      |:--:|
      |*Select Digitiser*|
      
   
   3. Create a new file by clicking on new -> select "ini" file -> Plant Description -> Reference Axes.
      
      |![2](https://user-images.githubusercontent.com/42251021/220801903-e0711069-038a-451f-8c31-3e0d4660d3b0.PNG) |
      |:--:|
      |*How to Create a New File*|
      
   4. Add Reference Axes Manually. (# followed by reference axes, numbers separated by commas without spaces; change H & V axes individually)
  
  ## Step 2:
   1. Download and keep both the python files in the same folder.
   2. Run parent.py from cmd.
   3. Give the Path to the point cloud.
  
  ## Step 3:
   1. Once the above steps are done properly and no errors received, you're ready to start digitising.
   2. Select the first node (node 0 usually) by pressing "n0" on keyboard.
   3. Select the points, on the point cloud. By pressing ```Shift + Left Click```
   4. The first selected point will be huge, don't get scared.<br />
      ### How to navigate through the Point Cloud <br />
      a. ```Shift + -``` to reduce the size of picked point.<br />
      b. ```Shift + +``` to increase the size of picked point.<br />
      c. ```Ctrl + -``` to reduce the size of all the points in the point cloud.<br />
      d. ```Ctrl + +``` to increase the size of all the points in the point cloud.<br />
      e. Scroll to zoom in and zoom out.<br />
      f. ```Ctrl + Left Click``` and drag the mouse to **Pan**.<br />
      g. ```Left Click``` and drag mouse to move the whole Point Cloud.<br />
      h. Sometimes a point does not register in the Floradig, you can select the same point again.<br />
   5. Repeat the process, there is no need to select the node again if the node name is same as before.<br />
   6. **Have Fun Digitising!!!**
        
