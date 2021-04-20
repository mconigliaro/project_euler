import re


def solve():
    digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
            'seventy', 'eighty', 'ninety']

    all_words = []
    for i in range(1, 1001):
        words = []
        num = i

        if i == 1000:
            words.append('one thousand')
        else:
            if num in range(100, 1000):
                words.append(f'{digits[int(num / 100)]} hundred')
                num = num % 100

        if num in range(1, 10):
            words.append(digits[num])
        elif num in range(10, 90, 10):
            words.append(tens[int(num / 10)])
        elif num in range(11, 20):
            words.append(teens[num % 10])
        elif num in range(21, 100):
            words.append(f'{tens[int(num / 10)]} {digits[num % 10]}')

        all_words.append(' and '.join(words))

    return len(re.sub(' ', '', ' '.join(all_words)))


def test():
    assert solve() == 21124
