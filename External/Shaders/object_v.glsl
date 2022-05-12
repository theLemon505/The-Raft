#version 410

in vec3 position;

out vec3 p_color;

uniform mat4 view;
uniform mat4 projection;
uniform mat4 model;

void main()
{
    p_color = position;
    gl_Position = vec4(position, 1) * model * view * projection;
}