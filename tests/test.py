from myPackage.jobs import myMainPackage

def test_fahrToKelv():
    '''
    make sure freezing is calculated correctly
    '''

    
    assert myMainPackage.fahrToKelv(32) == 273.15, 'incorrect freezing point!'
