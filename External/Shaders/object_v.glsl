#version 330 core

layout (location=0) in vec3 vertexPosition;

out vec3 p_color;

void main()
{
    p_color = vertexPosition;
    gl_Position = vec4(vertexPosition, 1);
}