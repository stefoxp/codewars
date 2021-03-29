function calculate(str) {
    str = str.split("plus").join("+");
    str = str.split("minus").join("-");

    return eval(str) + "";
}