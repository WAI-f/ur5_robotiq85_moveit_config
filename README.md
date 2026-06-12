## UR5+robotiq2f_85 moveit setup

### 环境配置
1. 系统环境配置
- ubuntu24.04

2. 软件环境配置
- ros2 jazzy
- ros-jazzy-xacro
- ros-jazzy-joint-state-publisher-gui
- ros-jazzy-moveit*


### 编译
1. 下载urdf仓库
```
git@github.com:WAI-f/ur5_robotiq85_description.git
```
2. 编译代码
```
cd ur5_robotiq85_description
colcon build
source install/setup.bash
```
3. 下载当前仓库代码
```
git@github.com:WAI-f/ur5_robotiq85_moveit_config.git
```
4. 编译代码
```
cd ur_robotiq_realsense_moveit_config
colcon build
source install/setup.bash
```

### 可视化
1. 启动rviz
```
ros2 launch ur_robotiq_realsense_moveit_config demo.launch.py
```


### 创建moveit_config package流程
1. 启动moveit setup assistant:
```
ros2 launch moveit_setup_assistant setup_assistant.launch.py
```
- **start screen**
    - 点击**Create New Moveit Configuration Package**
    - 点击**Browser**, 选择ur5_robotiq85_rsd455.urdf.xacro所在路径
    - 点击**Load Files**, 正常加载会提示100%

- **self collisions**
    - 调整**Sampling Density**滑动条，数值越大采样密度越大，计算越准，但是计算速度也越慢
    - 点击**Generate Collision Matrix**

- **Virtual Joints**
    - 点击**Add Virtual Joint**按钮添加虚拟关节，这里是给world坐标系和机械臂base坐标系之间添加一个虚拟关节

- **Planning Groups**
    - 点击**Add group**添加ur arm group
    - 点击**Add group**添加hand group

- **Robot Poses**
    - 点击**Add Pose**添加home pose
    - 点击**Add Pose**添加detect pose
    - 点击**Add Pose**添加open pose
    - 点击**Add Pose**添加close pose

- **End Effectors**
    - 点击**Add End Effector**添加hand effector

- **Passive Joints**
    - 添加一些不参与规划的joint

- **ros2_control_URDF Modifications**
    - 点击**Add interface**按钮即可

- **ROS2 controllers**
    - 点击**Add controller**按钮添加ur arm controller:
        - 再点击**Add Planning Group Joints**, 添加ur arm group
    - 点击**Add controller**按钮添加hand controller:
        - 再点击**Add Planning Group Joints**, 添加hand group

- **Moveit controllers**
    - 设置和**ROS2 controllers**完全一致
    - 点击**Add controller**按钮添加ur arm controller:
        - 再点击**Add Planning Group Joints**, 添加ur arm group
    - 点击**Add controller**按钮添加hand controller:
        - 再点击**Add Planning Group Joints**, 添加hand group

- **Perception**
    - 主要是给相机感知模块做的设置，可以参考我的设置，也可以不设置，当前无影响

- **Launch Files**
    - 按照默认设置即可

- **Author Information**
    - 设置个人信息，按照个人需求填写即可

- **Configuration Files**
    - 点击**Browser**按钮，设置moveit_config保存路径
    - 点击**Generate Package**，进度条显示100%即完整整个config的配置
    - 点击**Exit Setup Assistant**退出gui

3. 修改配置文件
- 按照步骤2生成的*moveit_config，在rviz2中做planning的时候会报错：
原因就是在config/joint_limits.yaml中没有设置加速度约束, 添加加速度约束即可


### 参考
- moveit setup assistant官方教程：[MoveIt Setup Assistant](https://moveit.picknik.ai/main/doc/examples/setup_assistant/setup_assistant_tutorial.html)