# logic.py

## relative\_intensity\_of\_auxiliary\_engine()

```python
from math import acos, cos, pi

def relative_intensity_of_auxiliary_engine(x, y, intensity):
    '''
    Given a point (x, y) and their hypotenuse, return what strength to apply to
    the auxiliary motor.
    '''
```

First, we normalize `x` by dividing by the intensity. This allows us to work with a unit circle. The result is `x'`. If `intensity` is zero, any value will end up with a (0, 0) engine speed; we've defaulted to zero.

Now, we take the absolute value of `x'`. With this, we work as if on the first quadrant, where the auxiliary engine value is in `[-1, 1]`, and the main engine is fixed at 1. Let's call this result `x_relative`.

```python
    try:
        x_relative = abs(x / intensity)
    except ZeroDivisionError:
        return 0
```

See the example below for `theta = π/2`. In this case, `aux` is expected to be 0.

    (1, 1)
      |
      |__
      |  ``-._  (1, 0)
      |       `.
      |      ,'|`.
      |    ,'  |  \
      |  ,'    |  `.
      |,'      |   |
      L........:....... (1, -1)
               |
          x_relative = 1/√2

You can see that, with a naive linear regression of `x_relative` to `aux`, we'd get a non-zero value for `aux` here.
This also has the disadvantage of being non-symmetrical when flipping to the other quadrants.

```python
    # aux = 1 - 2 * x_relative
```

To solve for `aux`, we must use `theta` instead of `x_relative`. We can get `theta = f(x_relative)`, and then map this
value to a function `g(theta) = g(f(x_relative))` that goes from -1 to 1.

    g(theta)
       |
     1 |                x
       |                :
       |                :
     0 |         x      :
       |         :      :
       |         :      :
    -1 |  x      :      :
       |  :      :      :
       L..:......:......:... theta = f(x_relative)
         -π      0      π

We can work out `f(x_relative) = 4 * acos(x_relative) - π` due to trigonometry. Now we have a few choices for `g(f(x_relative))`:

1. First option is to make a linear regression. This would make `g(f(x_relative)) = f(x_relative) / π`. The full formula then becomes:

  ```python
      # aux = (4 * acos(x_relative) - pi) / pi
  ```

  We get both symmetry and full range movement, but the problem is that we still get pretty sharp changes around the edges of quadrants.

2. Another option is to map these speed changes to a sine wave, making them more natural around the edges of quadrants, thus respecting the original circular format of the control. We get `g(f(x_relative)) = sin(x_relative/2)`, which can be simplified to:

  ```python
      aux = -cos(2 * acos(x_relative))
      return aux
  ```

## direction\_event\_to\_engine\_input()

```python
def direction_event_to_engine_input(event: DirectionEvent):
    '''
    Get a position in a circle and transform into left/right engine powers.
    '''
```

The main motor `l` will have a fixed speed (`l = 1`), and the auxiliary motor `r` will set the direction that the car will drive. We use the method described in the previous section for the auxiliary motor.

```python
    (x, y) = event.get_coordinates()
    intensity = hypot(x, y)

    l = 1
    r = relative_intensity_of_auxiliary_engine(x, y, intensity)
    assert abs(r) <= 1
```

The range of positions and trivial engine powers are as follows below:

                          (1, 1)
                            |
                          __|__
             (0, 1)  _.-''  |  ``-._  (1, 0)
                   ,'       |       `.
                 ,'         |         `.
                /  Quad. 2  |  Quad. 1  \
               .'           |           `.
               |            |            |
    (-1, 1) ................+................ (1, -1)
               |            |            |
               \            |            /
                \  Quad. 3  |  Quad. 4  /
                 `.         |         ,'
          (-1, 0)  ._       |       _,  (0, -1)
                     `._    |    _.'
                        `'--+--''
                            |
                        (-1, -1)

This has a 4-way simmetry. We assume quadrant 1 to calculate (l, r), with l = 1 and r being the auxiliary engine (range `[-1, 1]`). Therefore, we can transform these values as follows:

           _,...._
        ,-'   |   `-.
      ,'      |      `.
     / (r, l) | (l, r) \
    /         |         \
    |.........+.........|
    \         |         /
     \(-l, -r)|(-r, -l)/
      \       |       /
       `._    |    _,'
          `-....,-'

The equivalent transformation is:

```python
    if is_on_left_half(x, y) ^ is_on_bottom_half(x, y):
        l, r = r, l

    if is_on_bottom_half(x, y):
        l = -l
        r = -r
```

In case `intensity` is greater than 1, we rectify this value when creating the ouput event.

```python
    return EngineInput(*to_engine_inputs(l, r, min(intensity, 1)))
```
