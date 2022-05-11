#version 410

in vec3 p_color;

out vec4 color;

void main()
{
    color = vec4(p_color+vec3(1,1,1), 1);
}