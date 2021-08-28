@app.route('/questions')
  def retrieve_questions():
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)

      categories = Category.query.order_by(Category.type).all()

      if len(current_questions) == 0:
          abort(404)

      return jsonify({
          'success': True,
          'questions': current_questions,
          'total_questions': len(selection),
          'categories': {category.id: category.type for category in categories},
          'current_category': None
      })