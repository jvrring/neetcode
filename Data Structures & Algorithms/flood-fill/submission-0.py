class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, colour: int) -> List[List[int]]:
        # remember colour of starting pixel
        original = image[sr][sc]

        # if new colour is same, we leave it alone
        if original == colour:
            return image

        # dfs recursion
        def dfs(r: int, c: int):
            # boundary check
            if not (0 <= r < len(image) and 0 <= c < len(image[0])):
                return

            # if pixel isn't the original one
            if image[r][c] != original:
                return 

            # change pixel to new colour
            image[r][c] = colour

            # recursively visit neighbouring pixeks
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        # start exploring the first pixel
        dfs(sr, sc)
        
        # return modified image
        return image
        


        

        
        