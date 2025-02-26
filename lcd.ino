#include <LiquidCrystal_I2C.h>


#define LCD_ADDR 0x27
#define LCD_COLUMNS 16
#define LCD_ROWS 2

LiquidCrystal_I2C lcd(LCD_ADDR, LCD_COLUMNS, LCD_ROWS);

void setup() {
    // put your setup code here, to run once:
    lcd.begin(16,2);
    lcd.init();
    lcd.backlight();

    lcd.setCursor(5,0);
    lcd.print("Hello");

    lcd.setCursor(0,1);
    lcd.print("The Best Robotics");
}

void loop() {
    // put your main code here, to run repeatedly:
}