#pragma once

class Vector1 {
public:
	Vector1();
	Vector1(int x, int y);
	~Vector1();
	int GetX() const;
private:
	int mX;
	int mY;
};