#version 410

in vec3 position;

out vec3 p_color;

void main()
{
    p_color = position;
    gl_Position = vec4(position, 1);
}