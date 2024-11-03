class Cardanimation:
    def __init__(self, card_pos, target_pos, animation_speed):
        self.card_pos = card_pos
        self.target_pos = target_pos
        self.animation_speed = animation_speed

    def card_animation(self):
        delta_x = self.target_pos[0] - self.card_pos[0]
        delta_y = self.target_pos[1] - self.card_pos[1]

        # Check if the card is close enough to stop
        if abs(delta_x) < self.animation_speed[0] and abs(delta_y) < self.animation_speed[1]:
            self.card_pos = list(self.target_pos)  # Snap to target position
            return self.card_pos

        # Calculate movement along x and y based on the speed
        move_x = min(abs(delta_x), self.animation_speed[0]) * (1 if delta_x > 0 else -1)
        move_y = min(abs(delta_y), self.animation_speed[1]) * (1 if delta_y > 0 else -1)

        # Update the card's position
        self.card_pos[0] += move_x
        self.card_pos[1] += move_y
        return self.card_pos
