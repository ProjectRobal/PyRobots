import pymunk
import math

def get_anchor(shape:pymunk.Shape):

    vertices=shape.get_vertices()

    left=vertices[0][0]
    right=vertices[0][0]
    top=vertices[0][1]
    bottom=vertices[0][1]

    for v in vertices:
        if v[0]<left:
            left=v[0]
        if v[0]>right:
            right=v[0]
        if v[1]>top:
            top=v[1]
        if v[1]<bottom:
            bottom=v[1]

    return pymunk.Vec2d((-left+right)/2,(top-bottom)/2)

def _to_pyglet_coords(anchor,shape,output):
    output.position=shape.body.position
    output.anchor_position=(-anchor[0],-anchor[1])
    output.rotation=-shape.body.angle*(180.0/math.pi)

def to_pyglet_coords(shape,output):

    _to_pyglet_coords(get_anchor(shape),shape,output)

