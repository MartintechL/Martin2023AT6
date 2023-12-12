class DataValidator:
    def validate_inputs(self, input_list):
        valid_integers = []

        for input_str in input_list:
            # Check if the input is a positive integer
            if input_str.isdigit() and int(input_str) > 0:
                valid_integers.append(int(input_str))

        return valid_integers
