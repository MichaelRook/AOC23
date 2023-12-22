from snowcalibrator import SnowCalibrator

if __name__ == "__main__":

    my_simple_calibrator = SnowCalibrator.construct_instance(include_words=False)
    result1 = my_simple_calibrator.sum_all_numbers()

    my_complex_calibrator = SnowCalibrator.construct_instance(include_words=True)
    result2 = my_complex_calibrator.sum_all_numbers()

    print(f"results1: {result1}, result2: {result2}")