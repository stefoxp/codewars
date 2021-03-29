CREATE FUNCTION increment(@dato int)
RETURNS @risultato int
AS
BEGIN
  SET @risultato = @dato + 1;
  
  RETURN @risultato;
END;
