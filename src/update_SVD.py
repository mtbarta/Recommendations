import src.SVD as SVD

class update_SVD(SVD):
    """Checklist: 1. Use folding-up method to update predictions
                2. store percent of new documents folded in, 
                    determine when to update.
                3. auto cross-validate for update response? """
    def add_new_rating(self,data_tuple):
        user, item, rating = data_tuple
        #if user > len(self.U):
        #    add_new_user()
    def add_new_user(self, user):
        #update U matrix with new_users*self.V
        #append to U.
        
        return
    def add_new_item(self):
        return

