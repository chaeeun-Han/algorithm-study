def solution(numer1, denom1, numer2, denom2):
    n = denom1*numer2 + denom2*numer1
    d = denom1 * denom2
    gcd_x, gcd_y = n, d
    
    while gcd_y:
        gcd_x, gcd_y = gcd_y, gcd_x % gcd_y

    return [n//gcd_x, d//gcd_x]