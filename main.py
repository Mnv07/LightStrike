from vehicle.skills.base_skill import Skill
from vehicle.skills.util import ui
import numpy as np

class Game(Skill):

    #Had to hardcode this -- should be replaced by light senor hardware output
    USER_SETTINGS = (
        ui.Slider(
          identifier="ssuccess_rate",
          label="Success Rate",
          detail="How many times the vehicle has been hit by the laser",
          min_value=0,
          max_value=20,
          value=0,
          units="'Successful Hits",
      ),
    )

    def __init__(self):
        super(Game, self).__init__()
        self.moving_autonomously = False

    def get_onscreen_controls(self, api):
      # Called to determine what UI to show in the mobile app during runtime
      if self.moving_autonomously:
        return dict(
          title="Moving autonomously!",
          strafe_buttons_enabled=False,
          height_slider_enabled=False,
          steering_enabled=False,
          drag_enabled=False,
          double_tap_enabled=False,
          prompt_buttons=[ui.Button(identifier="stop", label="Stop", style="danger")]
        )
      else:
        return dict(
          title="Start moving?",
          strafe_buttons_enabled=True,
          height_slider_enabled=True,
          steering_enabled=True,
          drag_enabled=True,
          double_tap_enabled=True,
          prompt_buttons=[ui.Button(identifier="start", label="Start", style="primary")]
        )

    def button_pressed(self, api, button_id):
        if button_id == "start":
            self.moving_autonomously = True
            api.focus.set_custom_subject(0,0,0)
            api.focus.set_keep_subject_in_sight(1)
            api.focus.set_range(3,1,1)
        elif button_id == "stop":
            self.moving_autonomously = False
        # tell the sdk that the get_onscreen_controls() method should be called again
        self.set_needs_layout()

    def update(self, api):
        # Called on every loop of the autonomy engine.
        if self.moving_autonomously:
            # Disable manual control during autonomous motion.
            api.phone.disable_movement_commands()

            # Move toward positoin at velocity of successes
            api.movement.set_max_speed(self.get_value_for_user_setting('success_rate'))

            # Move diagonally
            api.movement.set_desired_pos_nav(
                np.array(
                   [10, 10, 10], dtype=np.float
                ),
                0.75)
        else:
            # Re-enable manual control
            api.phone.enable_movement_commands()
