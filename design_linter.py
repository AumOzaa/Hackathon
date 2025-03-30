class DesignLinter:
    def check_colors(self, styles):
        errors = []
        for style in styles:
            if style["style_type"] == "FILL":
                if style["color"]["contrast"] < 4.5:  # WCAG AA standard
                    errors.append(f"Low contrast: {style['name']} (Contrast: {style['color']['contrast']})")
        return errors

    def check_fonts(self, text_styles):
        errors = []
        for style in text_styles:
            if style["fontSize"] < 12:
                errors.append(f"Font too small: {style['name']} ({style['fontSize']}px)")
        return errors