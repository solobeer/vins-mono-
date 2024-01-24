cmake_minimum_required(VERSION 2.8.3)
project(feature_tracker)

set(CMAKE_BUILD_TYPE "DEBUG")
set(CMAKE_CXX_FLAGS "-std=c++11")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -Wall -g")

find_package(catkin REQUIRED COMPONENTS
    rospy
    roscpp
    std_msgs
    sensor_msgs
    cv_bridge
    camera_model
    )

find_package(OpenCV REQUIRED)

# find_package(Python REQUIRED)

# set(CMAKE_PREFIX_PATH "/home/hzb/libtorch")
# # set(Torch_DIR "/home/hzb/libtorch/share/cmake")
# find_package(Torch REQUIRED)

# include_directories(${TORCH_INCLUDE_DIRS})

# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
# set(PYTHON_INCLUDE_DIRS "/usr/include/python3.6m")
# set(Python_LIBRARIES "/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu/")
# include_directories(
#     ${PYTHON_INCLUDE_DIRS}
#     # "/home/hzb/anaconda3/envs/py310/lib/python3.10/site-packages/torch/include/"
# )

catkin_package()

include_directories(
    ${catkin_INCLUDE_DIRS}
    )

set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)
find_package(Eigen3)
include_directories(
  ${catkin_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIR}
)

add_executable(feature_tracker
    src/feature_tracker_node.cpp
    src/parameters.cpp
    src/feature_tracker.cpp
    # src/feature_tracker_ai.cpp
    )

target_link_libraries(feature_tracker ${catkin_LIBRARIES} ${OpenCV_LIBS})
target_link_libraries(feature_tracker ${Python_LIBRARIES} python3.6m ${TORCH_LIBRARIES})
