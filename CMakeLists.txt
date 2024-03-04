cmake_minimum_required(VERSION 3.28)
project(maze-solver)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wfatal-errors") 
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_BUILD_TYPE Debug)


set(CMAKE_CXX_STANDARD_REQUIRED ON)
include(FetchContent)
FetchContent_Declare(
  raylib
	GIT_REPOSITORY https://github.com/raysan5/raylib.git 
	GIT_SHALLOW TRUE
	GIT_PROGRESS TRUE
)
FetchContent_MakeAvailable(raylib)

file(GLOB_RECURSE SRC_FILES src/*.cpp) 
add_executable(maze ${SRC_FILES})

target_include_directories(maze PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}/include")
target_link_libraries(maze PRIVATE raylib)
